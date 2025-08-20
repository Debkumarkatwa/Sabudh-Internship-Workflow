'''
Write a function to generate an m+1 dimensional data set, of size n, consisting of m continuous independent
variables (X) and one dependent binary variable (Y) defined as
Y =
{1 if p(y = 1|~x) = 1
1+exp−~x.~β > 0.5
0 otherwise
where,
• β is a random vector of dimensionality m + 1, representing the coefficients of the linear relationship
between X and Y, and
• ∀i ∈[1,n],xi0 = 1
To add noise to the labels (Y) generated, we assume a Bernoulli distribution with probability of success, θ,
that determines whether or not the label generated, as above, is to be flipped. The larger the value of θ, the
greater is the noise.
The function should take the following parameters:
• θ: The probability of flipping the label, Y
• n: The size of the data set
• m: The number of indepedent variables
Output from the function should be:
• X: An n × m numpy array of independent variable values (with a 1 in the first column)
• Y : The n × 1 binary numpy array of output values
• β: The random coefficients used to generate Y from X
'''

import numpy as np
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


# Example usage:
if __name__ == "__main__":
    X, Y, beta = generate_data(0.1, 100, 3)
    # print("X:", X)
    # print("Y:", Y)
    print("Beta:", beta)
