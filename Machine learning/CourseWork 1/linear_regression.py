import numpy as np
import pandas as pd

'''
1 Write a function to generate an m+1 dimensional data set, of size n, consisting of m continuous independent
variables (X) and one dependent variable (Y) defined as
yi = xiβ + e
where,
• e is a Gaussuan distribution with mean 0 and standard deviation (σ), representing the unexplained
variation in Y
• β is a random vector of dimensionality m + 1, representing the coefficients of the linear relationship
between X and Y, and
• ∀i ∈[1,n],xi0= 1
The function should take the following parameters:
• σ: The spread of noise in the output variable
• n: The size of the data set
• m: The number of indepedent variables
Output from the function should be:
• X: An n ×m numpy array of independent variable values (with a 1 in the first column)
• Y : The n ×1 numpy array of output values
• β: The random coefficients used to generatre Y from X
'''
def generate_data(sigma: float, n: int, m: int):
    beta_true = np.random.randn(m + 1, 1)
    X_independent = np.random.rand(n, m) * 10 # Multiplying by 10 to get a wider range of values

    X = np.hstack((np.ones((n, 1)), X_independent))
    noise = np.random.normal(0, sigma, (n, 1))
    Y = np.dot(X, beta_true) + noise

    return X, Y, beta_true


# Example usage
X, Y, beta = generate_data(sigma=1.0, n=5, m=3)

print("X:---------\n", X)
print("\nY:-----------\n", Y)
print("\nBeta:---------\n", beta)

'''
2 Write a function that learns the parameters of a linear regression line given inputs
• X: An n ×m numpy array of independent variable values
• Y : The n ×1 numpy array of output values
• k: the number of iteractions (epochs)
• τ: the threshold on change in Cost function value from the previous to current iteration
• λ: the learning rate for Gradient Descent
The function should implement the Gradient Descent algorithm as discussed in class that initialises β with
random values and then updates these values in each iteraction by moving in the the direction defined by
the partial derivative of the cost function with respect to each of the coefficients. The function should use
only one loop that ends after a number of iterations (k) or a threshold on the change in cost function value
(τ).
The output should be an m + 1 dimensional vector of coefficients and the final cost function value.
'''
def gradient_descent(X: np.ndarray, Y: np.ndarray, k: int, T: float, learning_rate: float):

    n_samples, n_features = X.shape # n_features will be m+1 (including intercept)

    beta_learned = np.random.randn(n_features, 1)
    previous_cost = float('inf')
    cost_history = []

    for iteration in range(k):
        predictions = np.dot(X, beta_learned)

        errors = predictions - Y

        current_cost = (1 / (2 * n_samples)) * np.sum(errors**2)
        cost_history.append(current_cost) # Add current cost to history

        gradient = (1 / n_samples) * np.dot(X.T, errors)

        beta_learned = beta_learned - learning_rate * gradient

        if abs(previous_cost - current_cost) < T:
            print(f"Convergence achieved at iteration {iteration}!\n")
            break

        previous_cost = current_cost

    else: # This block executes if the loop completes without 'break'
        print(f"Gradient Descent completed {k} iterations without converging below threshold T.")

    return beta_learned, current_cost

# Example usage:
np.random.seed(42)
n, m = 10, 3
X = np.ones((n, m))
X[:, 1:] = np.random.rand(n, m - 1)
Y = np.random.rand(n)

beta, final_cost = gradient_descent(X, Y, k=1000, T=1e-6, learning_rate=0.1)

print("Learned coefficients:-------\n", beta)
print("\nFinal cost:-------\n", final_cost)







'''
3 Create a report investigating how differen values of n and σ impact the ability for your linear regression
function to learn the coefficients, β, used to generate the output vector Y .
'''
def generate_data(sigma: float, n: int, m: int):
    beta_true = np.random.randn(m + 1, 1)
    X_independent = np.random.rand(n, m) * 10 # Multiplying by 10 to get a wider range of values

    X = np.hstack((np.ones((n, 1)), X_independent))
    noise = np.random.normal(0, sigma, (n, 1))
    Y = np.dot(X, beta_true) + noise

    return X, Y, beta_true


def gradient_descent(X: np.ndarray, Y: np.ndarray, k: int, T: float, learning_rate: float):

    n_samples, n_features = X.shape # n_features will be m+1 (including intercept)

    beta_learned = np.random.randn(n_features, 1)
    previous_cost = float('inf')
    cost_history = []

    for iteration in range(k):
        predictions = np.dot(X, beta_learned)

        errors = predictions - Y

        current_cost = (1 / (2 * n_samples)) * np.sum(errors**2)
        cost_history.append(current_cost) # Add current cost to history

        gradient = (1 / n_samples) * np.dot(X.T, errors)

        beta_learned = beta_learned - learning_rate * gradient

        # if abs(previous_cost - current_cost) < T:
        #     print(f"Convergence achieved at iteration {iteration}!\n")
        #     break

        previous_cost = current_cost

    # else: # This block executes if the loop completes without 'break'
    #     print(f"Gradient Descent completed {k} iterations without converging below threshold T.")

    return beta_learned, current_cost

if __name__ == "__main__":
    n_values = [10, 50, 80, 100, 500]
    sigma_values = [0.01, 0.1, 0.5, 1.0, 2.0]
    results = []

    m_features = 3

    print("--- Running Experiments for Report ---")
    for n in n_values:
        for sigma in sigma_values:
            # Generate data for the current n and sigma
            X, Y, beta_true = generate_data(sigma, n, m=m_features)

            beta_learned, final_cost = gradient_descent(X, Y, k=10000, T= 1e-6 , learning_rate=0.01)

            # Calculate Mean Absolute Error (MAE) between true and learned coefficients
            mae = np.mean(np.abs(beta_true - beta_learned))

            results.append({
                "n": n,
                "sigma": sigma,
                "MAE": mae,
                "Final_Cost": final_cost
            })

            print(f"Completed: {n} || {sigma:.2f} || {mae:.4f}")

    df_results = pd.DataFrame(results)
    print("\n--- Experiment Results DataFrame ---")
    print(df_results)
