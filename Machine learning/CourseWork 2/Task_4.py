'''
Add L1 and L2 regularization to the Logistic Regression cost function. How does this impact the models
learnt? How does the choice of regularization constant impact the β vector learned?
'''

import numpy as np
from Task_1 import generate_data
import matplotlib.pyplot as plt
import seaborn as sns


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
'''


def logistic_regression_with_regularization(X, Y, k, tau, lambda_, regularization='L2'):
    n, m = X.shape
    beta = np.random.randn(m)  # Initialize coefficients with random values
    prev_cost = float('inf')  # Previous cost function value

    for i in range(k):
        # Calculate the linear combination
        linear_combination = X @ beta

        # Calculate probabilities using the logistic function
        probabilities = 1 / (1 + np.exp(-linear_combination))

        # Calculate the cost function (cross-entropy loss)
        cost = -np.mean(Y * np.log(probabilities.reshape(-1, 1)) + (1 - Y) * np.log(1 - probabilities.reshape(-1, 1)))

        # Add regularization term
        if regularization == 'L2':
            cost += lambda_ * np.sum(beta[1:] ** 2) / (2 * n)  # Exclude intercept term
        elif regularization == 'L1':
            cost += lambda_ * np.sum(np.abs(beta[1:])) / n  # Exclude intercept term

        # Check for convergence based on change in cost
        if abs(prev_cost - cost) < tau:
            break

        prev_cost = cost

        # Calculate the gradient
        gradient = X.T @ (probabilities.reshape(-1, 1) - Y) / n

        # Add regularization gradient
        if regularization == 'L2':
            gradient[1:] += (lambda_ * beta[1:] / n).reshape(-1, 1)  # Exclude intercept term and reshape
        elif regularization == 'L1':
            gradient[1:] += (lambda_ * np.sign(beta[1:]) / n).reshape(-1, 1)  # Exclude intercept term and reshape

        # Update coefficients using gradient descent
        beta -= lambda_ * gradient.flatten()  # Flatten the gradient to match beta's shape

    return beta, cost

# Example usage:
if __name__ == "__main__":
    X, Y, beta = generate_data(0.1, 100, 3)

    # Test L2 regularization
    beta_l2, final_cost_l2 = logistic_regression_with_regularization(X, Y, 1000, 1e-6, 0.01, regularization='L2')
    print("L2 Regularization - Final coefficients:", beta_l2)
    print("L2 Regularization - Final cost:", final_cost_l2)

    # Test L1 regularization
    beta_l1, final_cost_l1 = logistic_regression_with_regularization(X, Y, 1000, 1e-6, 0.01, regularization='L1')
    print("L1 Regularization - Final coefficients:", beta_l1)
    print("L1 Regularization - Final cost:", final_cost_l1)

    # Visualize the coefficients
    plt.figure(figsize=(12, 6))
    sns.barplot(x=np.arange(len(beta_l2)), y=beta_l2, color='blue', alpha=0.6, label='L2 Regularization')
    sns.barplot(x=np.arange(len(beta_l1)), y=beta_l1, color='red', alpha=0.6, label='L1 Regularization')
    plt.title('Comparison of Coefficients with L1 and L2 Regularization')
    plt.xlabel('Coefficient Index')
    plt.ylabel('Coefficient Value')
    plt.legend()
    plt.show()



'''
Observations:
1. L2 regularization tends to shrink the coefficients towards zero, especially for those that are less significant, while still keeping all features in the model.
2. L1 regularization can lead to sparse solutions, effectively setting some coefficients to zero, which can be useful for feature selection.
3. The choice of regularization constant (lambda_) significantly impacts the coefficients learned. A larger lambda_ will increase the penalty for larger coefficients, leading to smaller values in the learned coefficients.
'''