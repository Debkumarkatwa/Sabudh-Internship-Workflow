"""
PART 6 : MODEL DEPLOYMENT (RESTful Web Service)
Predicting the Price of a Football Player
-----------------------------------------
This script creates a Flask REST API that loads the final trained model
and predicts the market value of a player based on input features.
"""

from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import joblib

# ==========================================
# 1. LOAD MODEL AND SCALER
# ==========================================
# Before running this, make sure you saved your best model (from Part 4)
# Example:
#   joblib.dump(model, "best_model.pkl")
#   joblib.dump(scaler, "scaler.pkl")

# Load model & scaler
model = joblib.load("best_model.pkl")
scaler = joblib.load("scaler.pkl")

# ==========================================
# 2. INITIALIZE FLASK APP
# ==========================================
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Football Player Market Value Prediction API is running!"})

# ==========================================
# 3. PREDICTION ENDPOINT
# ==========================================
@app.route('/predict', methods=['POST'])
def predict():
    """
    Accepts JSON input like:
    {
        "age_clean": 25,
        "page_views_clean": 40000,
        "fpl_value_clean": 7.5,
        "fpl_sel_clean": 15,
        "fpl_points_clean": 180,
        "position_cat": 2,
        "region": 2,
        "big_club": 1,
        "new_signing": 0
    }
    """
    data = request.get_json()

    # Convert to DataFrame
    input_df = pd.DataFrame([data])

    # Scale numeric data using previously fitted scaler
    input_scaled = scaler.transform(input_df)

    # Predict market value
    prediction = model.predict(input_scaled)
    pred_value = float(prediction[0])

    return jsonify({
        "predicted_market_value": round(pred_value, 2),
        "status": "success"
    })

# ==========================================
# 4. RUN THE APP
# ==========================================
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
