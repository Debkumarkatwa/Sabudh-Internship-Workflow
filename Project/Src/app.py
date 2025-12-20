# ============================================================
# 0. IMPORTS
# ============================================================
import numpy as np
import cv2
from PIL import Image
import torch
from torchvision import models, transforms
from facenet_pytorch import MTCNN
import timm
from tensorflow import keras
import gradio as gr

# ============================================================
# 1. DEVICE SETUP
# ============================================================
device = "cuda" if torch.cuda.is_available() else "cpu"
print("Using device:", device)
torch.backends.cudnn.benchmark = False

# ============================================================
# 2. FACE DETECTOR
# ============================================================
mtcnn = MTCNN(
    image_size=224,
    margin=20,
    keep_all=True,
    device=device
)

# ============================================================
# 3. ViT MODEL (EMBEDDINGS)
# ============================================================
vit_model = timm.create_model("vit_base_patch16_224", pretrained=True)
vit_model.head = torch.nn.Identity()
vit_model.to(device)
vit_model.eval()

vit_transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

# ============================================================
# 4. RESNET MODEL (EMBEDDINGS)
# ============================================================
resnet = models.resnet50(
    weights=models.ResNet50_Weights.IMAGENET1K_V2
)
resnet.fc = torch.nn.Identity()
resnet.to(device)
resnet.eval()

resnet_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

# ============================================================
# 5. LOAD CLASSIFIERS (ROOT DIRECTORY)
# ============================================================
VIT_classifier = keras.models.load_model("final_vit_classifier.keras")
RESNET_classifier = keras.models.load_model("final_resnet_classifier.keras")

# ============================================================
# 6. FACE UTILITIES
# ============================================================
def resize_fixed(pil_img, max_size=800):
    """Resize while maintaining aspect ratio."""
    w, h = pil_img.size
    if w > max_size:
        scale = max_size / w
        new_w = max_size
        new_h = int(h * scale)
        return pil_img.resize((new_w, new_h))
    return pil_img
def detect_faces(image_bgr):
    img_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    boxes, _ = mtcnn.detect(img_rgb)
    if boxes is None:
        return []
    return boxes.astype(int)

def crop_face(image_bgr, box):
    x1, y1, x2, y2 = box
    return image_bgr[y1:y2, x1:x2]

# ============================================================
# 7. EMBEDDING EXTRACTION
# ============================================================
def get_vit_embedding(face_bgr):
    img = Image.fromarray(cv2.cvtColor(face_bgr, cv2.COLOR_BGR2RGB))
    img = img.resize((224, 224))
    img_tensor = vit_transform(img).unsqueeze(0).to(device)

    with torch.no_grad():
        emb = vit_model(img_tensor)

    return emb.cpu().numpy().flatten()

def get_resnet_embedding(face_bgr):
    img = Image.fromarray(cv2.cvtColor(face_bgr, cv2.COLOR_BGR2RGB))
    img_tensor = resnet_transform(img).unsqueeze(0).to(device)

    with torch.no_grad():
        emb = resnet(img_tensor)

    return emb.cpu().numpy().flatten()

# ============================================================
# 8. CLASSIFICATION
# ============================================================

def classify_embedding(embedding, model_type):
    embedding = embedding.reshape(1, -1)

    if model_type == "ViT Model":
        pred = VIT_classifier.predict(embedding, verbose=0)[0][0]
        label = "Fake" if pred >= 0.5 else "Real"
        confidence = pred if label == "Fake" else 1 - pred

    elif model_type == "ResNet Model":
        pred = RESNET_classifier.predict(embedding, verbose=0)[0][0]
        label = "Fake" if pred >= 0.5 else "Real"
        confidence = pred if label == "Fake" else 1 - pred

    else:
        raise ValueError(f"Unknown model type: {model_type}")

    return label, float(confidence)


# ============================================================
# 9. DRAW BOUNDING BOX
# ============================================================
def draw_box(image, box, label):
    x1, y1, x2, y2 = box
    color = (0, 255, 0) if label == "Real" else (0, 0, 255)
    cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
    cv2.putText(
        image,
        label,
        (x1, max(0, y1 - 10)),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        color,
        2
    )

# ============================================================
# 10. BACKEND PIPELINE
# ============================================================
def BackEnd_Pipeline(model, image):
    if image is None:
        return [["-", "No Image", 0.0]], None

    img_bgr = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    boxes = detect_faces(img_bgr)

    if len(boxes) == 0:
        return [["-", "No faces detected", 0.0]], np.array(image)

    output = img_bgr.copy()
    results = []

    for idx, box in enumerate(boxes):
        face = crop_face(img_bgr, box)
        x1, y1, x2, y2 = box
        h, w, _ = img_bgr.shape
        x1, y1 = max(0, x1), max(0, y1)
        x2, y2 = min(w, x2), min(h, y2)
        face = img_bgr[y1:y2, x1:x2]


        if face.size == 0:
            results.append([idx + 1, "Invalid face", 0.0])
            continue

        emb = get_vit_embedding(face) if model == "ViT Model" else get_resnet_embedding(face)
        label, conf = classify_embedding(emb, model)

        x1, y1, x2, y2 = map(int, box)
        color = (0, 255, 0) if label == "Real" else (0, 0, 255)
        

        cv2.rectangle(output, (x1, y1), (x2, y2), color, 2)
        cv2.putText(
            output,
            f"{label} {conf:.3f}",
            (x1, max(10, y1 - 10)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            color,
            2
        )

        results.append([idx + 1, label, conf])

    out_pil = Image.fromarray(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
    return results, np.array(out_pil)

# ============================================================
# 11. UI – HOME PAGE
# ============================================================
with gr.Blocks(title="Deep Fake Identification") as home_page:

    gr.Markdown(
        """
        # Deep Fake Identification
        ### Detecting forged media using advanced deep learning models
        """
    )

    gr.Markdown("---")

    # Model Information Section
    gr.Markdown(
                """
This is a platform where you can identify difference between deepfakes and real images by simply uploading it to our plaform.
""")
    with gr.Row():

      with gr.Column():
            gr.Markdown(
                """

📌 How to Use

1. Select the desired model (ResNet or ViT).

2. Upload an image (single face or group photo).

3. Click Run Detection.

4. The system will display:

  ->Face Index

  -> Predicted Label (Real / Fake)

  -> Confidence Score
                """
            )
      with gr.Column():
            gr.Markdown(
        """📝Usage Tips

1. Upload clear, front-facing images for better accuracy

2. Avoid very low-resolution or heavily blurred images

3. Group images are supported — each face is analyzed individually

4. Higher confidence indicates stronger model certainty
""")
    gr.Markdown("---")

    # Advertisement / Showcase Section
    gr.Markdown(
        """
        ## 📢 Model Showcase
        Here we provide an image for demonstration purpose to show how the deep fake system works. 
        Upload the image for detection, select the model, ViT or ResNet and then you will see the result as Real or Fake label of the image's face
        """
    )

    # Changed to a static image display with the downloaded example image
    with gr.Row():

      with gr.Column():
        # Changed to a static image display with the downloaded example image
        showcase_upload = gr.Image(label="Example Combined Real & Fake Image", interactive=False, value='Demo_image.jpeg', height="200px")
      with gr.Column():
          showcase_upload = gr.Image(label="Output of the Image", interactive=False, value='op_image.jpeg', height="200px")


    gr.Markdown(
        """
        This section visually demonstrates the robustness of our deepfake detection system.
        """
    )

    gr.Markdown("---")
# Navigation Button
    navigate_btn = gr.Button("➡️ Navigate to the 'Detect' tab to run predictions", variant="primary")
    navigate_btn.click(lambda: gr.Info("Please click on the '🔍 Detect' tab at the top of the page to start deepfake detection."), inputs=[], outputs=[])



# ============================================================
# 12. UI – DETECT PAGE
# ============================================================

with gr.Blocks() as detect_page:
    gr.Markdown("# 🔍 Multi-face Deepfake Detector (ViT + ResNet)")

    model_choice = gr.Dropdown(
        ["ViT Model", "ResNet Model"],
        value="ViT Model",
        label="Choose Model"
    )

    img_input = gr.Image(type="pil", label="Upload Image",height="400px")
    submit_btn = gr.Button("Detect")

    results_table = gr.Dataframe(headers=["face_index", "label", "confidence"],
                                 datatype=["number", "text", "number"],
                                 label="Detections")

    img_output = gr.Image(label="Processed Image",height="500px")


    submit_btn.click(
        fn=BackEnd_Pipeline,
        inputs=[model_choice, img_input],
        outputs=[results_table, img_output]
    )

# ============================================================
# 13. TAB INTERFACE
# ============================================================
app = gr.TabbedInterface(
    [home_page, detect_page],
    ["🏠 Home", "🔍 Detect"]
)

app.launch(server_name="0.0.0.0", server_port=7860)
