'''
Write a function that learns the parameters of a logistic regression function given inputs
• X: An n × m numpy array of independent variable values
• Y : The n × 1 binary numpy array of output values
• k: the number of iteractions (epochs)
• τ: the threshold on change in Cost function value from the previous to current iteration
• λ: the learning rate for Gradient Descent
The function should implement the Gradient Descent algorithm as discussed in class that initialises β with
random values and then updates these values in each iteraction by moving in the the direction defined by
the partial derivative of the cost function with respect to each of the coefficients. The function should use
only one loop that ends after a number of iterations (k) or a threshold on the change in cost function value
(τ).
The output should be a m + 1 dimensional vector of coefficients and the final cost function value.
'''

from Task_1 import generate_data
import numpy as np
def logistic_regression(X, Y, k, tau, lambda_):
    n, m = X.shape
    beta = np.random.randn(m)  # Initialize coefficients with random values
    prev_cost = float('inf')  # Previous cost function value

    for i in range(k):
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


# Example usage:
if __name__ == "__main__":
    X, Y, beta = generate_data(0.1, 100, 3)
    beta, final_cost = logistic_regression(X, Y, 1000, 1e-6, 0.01)
    print("Final coefficients:", beta)
    print("Final cost:", final_cost)
