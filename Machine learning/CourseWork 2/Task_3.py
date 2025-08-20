'''
Create a report investigating how differen values of n and θ impact the ability for your logistic regression
function to learn the coefficients, β, used to generate the output vector Y . Also include your derivation of
the partial derivative of the cost function with respect to the parameters of the model.
'''

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from Task_1 import generate_data
from Task_2 import logistic_regression

'''
def generate_data(theta, n, m):

    beta = np.random.randn(m + 1)   # random coefficients β

    X = np.random.randn(n, m)   # independent variables X
    X = np.hstack((np.ones((n, 1)), X))  # Adding column of ones for the intercept

    # Calculate the linear combination ~x . ~β
    linear_combination = X @ beta

    # Calculate probabilities p(y = 1 | ~x)
    probabilities = 1 / (1 + np.exp(-linear_combination))

    # Generate binary labels Y based on the probabilities
    Y = (probabilities > 0.5).astype(int)

    # Flip labels with probability θ
    flip_mask = np.random.rand(n) < theta
    Y[flip_mask] = 1 - Y[flip_mask]

    return X, Y.reshape(-1, 1), beta

def logistic_regression(X, Y, k, tau, lambda_):
    n, m = X.shape
    beta = np.random.randn(m)  # Initialize coefficients with random values
    prev_cost = float('inf')  # Previous cost function value

    for epoch in range(k):
        # Calculate the linear combination
        linear_combination = X @ beta

        # Calculate probabilities using the logistic function
        probabilities = 1 / (1 + np.exp(-linear_combination))

        # Calculate the cost function (cross-entropy loss)
        # Reshape probabilities to (n, 1) for element-wise operations with Y
        cost = -np.mean(Y * np.log(probabilities.reshape(-1, 1)) + (1 - Y) * np.log(1 - probabilities.reshape(-1, 1)))


        # Check for convergence based on change in cost
        if abs(prev_cost - cost) < tau:
            break

        prev_cost = cost

        # Calculate the gradient
        # Reshape probabilities to (n, 1) for subtraction with Y
        gradient = X.T @ (probabilities.reshape(-1, 1) - Y) / n

        # Update coefficients using gradient descent
        beta -= lambda_ * gradient.flatten() # Flatten the gradient to match beta's shape

    return beta, cost
'''

def cosine_similarity(a, b):
    a = np.asarray(a).ravel()
    b = np.asarray(b).ravel()
    denom = (np.linalg.norm(a) * np.linalg.norm(b))
    if denom == 0:
        return np.nan
    return float(np.dot(a, b) / denom)

def report_investigation(n_values, theta_values, k=1000, tau=1e-6, lambda_=0.01):
    results = []

    for n in n_values:
        for theta in theta_values:
            # Generate data
            X, Y, beta_true = generate_data(theta, n, 3)

            # Learn coefficients using logistic regression
            beta_learned, final_cost = logistic_regression(X, Y, k, tau, lambda_)

            # Calculate error between true and learned coefficients
            error = np.linalg.norm(beta_true - beta_learned)
            cos = cosine_similarity(beta_true, beta_learned)
            probs = 1 / (1 + np.exp(-(X @ beta_learned)))
            y_pred = (probs > 0.5).astype(int).reshape(-1, 1)
            acc = (y_pred == Y).mean()

            results.append({
                'n': n,
                'theta': theta,
                'beta_true': beta_true,
                'beta_learned': beta_learned,
                'cosine_similarity': cos,
                'accuracy': acc,
                'error': error,
                'final_cost': final_cost
            })

    return results


def plot_report(df):
    
    sns.set(style="whitegrid", palette="muted", font_scale=1.1)

    # 1. Cosine similarity vs n (colored by θ)
    plt.figure(figsize=(7,5))
    sns.lineplot(data=df, x="n", y="cosine_similarity", hue="theta", marker="o")
    plt.title("Effect of n and θ on Cosine Similarity (β̂ vs β)")
    plt.show()

    # 2. Error norm vs n (colored by θ)
    plt.figure(figsize=(7,5))
    sns.lineplot(data=df, x="n", y="error", hue="theta", marker="o")
    plt.title("Effect of n and θ on Error Norm ‖β-β̂‖")
    plt.show()

    # 3. Final cost vs θ (colored by n)
    plt.figure(figsize=(7,5))
    sns.lineplot(data=df, x="theta", y="final_cost", hue="n", marker="o")
    plt.title("Effect of θ and n on Final Cost")
    plt.show()


# Example usage:
if __name__ == "__main__":
    n_values = [50, 100, 200]
    theta_values = [0.0, 0.1, 0.2, 0.5]
    
    results = report_investigation(n_values, theta_values)
    data = pd.DataFrame(results) # Convert the list to a DataFrame

    for result in results:
        print(f"N: {result['n']}, Theta: {result['theta']}\n "
            f"True β: {result['beta_true']}\n "
            f"Learned β: {result['beta_learned']}\n"
            f"Cosine Similarity: {result['cosine_similarity']:.4f}\n"
            f"Accuracy: {result['accuracy']:.4f}\n"
            f"Error: {result['error']:.4f}\n"
            f"Final Cost: {result['final_cost']:.4f}\n"
            "----------------------------------------------"
        )

    plot_report(data)

'''
Observations:------------------------------------------
 - Increasing n consistently improves cosine similarity and reduces error.
 - Increasing theta (label noise) decreases cosine similarity and accuracy, and raises the final cost.
 - With large n, the model resists small noise, but high theta still prevents recovering the true beta.
 - The model's performance is sensitive to both n and theta, with larger n generally leading to better learning.
 - The model can learn well with low noise (beta < 0.2) and moderate n, but struggles with high noise or small n.
 - The final cost function value decreases as n increases, indicating better convergence with more data.
'''