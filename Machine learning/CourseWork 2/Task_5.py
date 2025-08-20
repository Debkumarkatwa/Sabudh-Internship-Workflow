'''
Merge the linear regression code base created in Exercise 1 and the logistic regression code base created in
this Excercise and create an object oriented code base that maximises reuse of code across the algorithms.
'''


import numpy as np

# Data generators
def generate_linear_data(sigma: float, n: int, m: int):
    """
    Generate synthetic linear regression dataset:
      y = Xβ + noise, with Gaussian noise N(0, sigma^2).
    - sigma: noise stddev
    - n: number of samples
    - m: number of independent variables
    Returns: (X, y, beta)
    """
    beta = np.random.randn(m + 1)  # include intercept
    X = np.random.randn(n, m)
    X = np.hstack((np.ones((n, 1)), X))  # intercept column
    y = X @ beta + sigma * np.random.randn(n)
    return X, y.reshape(-1, 1), beta


def generate_logistic_data(theta: float, n: int, m: int):
    """
    Generate synthetic logistic regression dataset:
      y = 1{ sigmoid(x·β) > 0.5 }, with optional label noise.
    - theta: probability of flipping label (noise)
    - n: number of samples
    - m: number of independent variables
    Returns: (X, y, beta)
    """
    beta = np.random.randn(m + 1)
    X = np.random.randn(n, m)
    X = np.hstack((np.ones((n, 1)), X))  # intercept
    probs = 1 / (1 + np.exp(-(X @ beta)))
    y = (probs > 0.5).astype(int)
    # flip labels with probability theta
    flip_mask = np.random.rand(n) < theta
    y[flip_mask] = 1 - y[flip_mask]
    return X, y.reshape(-1, 1), beta



# Shared utilities
def _sigmoid(z: np.ndarray) -> np.ndarray:
    out = np.empty_like(z, dtype=float)
    pos = z >= 0
    neg = ~pos
    out[pos] = 1.0 / (1.0 + np.exp(-z[pos]))
    ez = np.exp(z[neg])
    out[neg] = ez / (1.0 + ez)
    return out


# Base class for Gradient Descent models
class BaseGDModel:
    """
    Base gradient-descent model with:
      - learning rate (lr), max_iter, tol (early stopping)
      - optional L1/L2 regularization (excluding intercept β0)
    Subclasses must implement _cost and _grad.
    """

    def __init__(self, lr=0.01, max_iter=1000, tol=1e-6,
                 reg=None, reg_strength=0.0, fit_intercept=True, random_state=None):
        self.lr = lr
        self.max_iter = max_iter
        self.tol = tol
        self.reg = None if reg is None else reg.lower()
        if self.reg not in (None, "l1", "l2"):
            raise ValueError("reg must be one of {None, 'l1', 'l2'}")
        self.reg_strength = float(reg_strength)
        self.fit_intercept = fit_intercept
        self.random_state = random_state

        self.beta_ = None
        self.cost_history_ = []
        self._n_cached = 1

    def fit(self, X: np.ndarray, y: np.ndarray):
        n, m = X.shape
        self._n_cached = n
        rng = np.random.default_rng(self.random_state)
        self.beta_ = rng.standard_normal(m)
        self.cost_history_.clear()

        prev_cost = np.inf
        for _ in range(self.max_iter):
            cost = self._cost(X, y, self.beta_)
            if self.reg:
                cost += self._reg_cost(self.beta_)
            self.cost_history_.append(float(cost))

            if abs(prev_cost - cost) < self.tol:
                break
            prev_cost = cost

            grad = self._grad(X, y, self.beta_)
            if self.reg:
                grad += self._reg_grad(self.beta_)
            self.beta_ -= self.lr * grad

        return self

    def _reg_cost(self, beta: np.ndarray) -> float:
        b = beta[1:]
        lam = self.reg_strength
        if self.reg == "l2":
            return lam * np.sum(b * b) / (2 * self._n_cached)
        elif self.reg == "l1":
            return lam * np.sum(np.abs(b)) / self._n_cached
        return 0.0

    def _reg_grad(self, beta: np.ndarray) -> np.ndarray:
        grad = np.zeros_like(beta)
        b = beta[1:]
        lam = self.reg_strength
        if self.reg == "l2":
            grad[1:] = lam * b / self._n_cached
        elif self.reg == "l1":
            grad[1:] = lam * np.sign(b) / self._n_cached
        return grad

    # hooks
    def _cost(self, X, y, beta): raise NotImplementedError
    def _grad(self, X, y, beta): raise NotImplementedError



# Linear Regression
class LinearRegressionGD(BaseGDModel):
    def _cost(self, X, y, beta):
        self._n_cached = X.shape[0]
        resid = X @ beta - y.ravel()
        return 0.5 * np.mean(resid * resid)

    def _grad(self, X, y, beta):
        resid = (X @ beta - y.ravel()).reshape(-1, 1)
        return (X.T @ resid).ravel() / X.shape[0]

    def predict(self, X):
        return X @ self.beta_


# Logistic Regression
class LogisticRegressionGD(BaseGDModel):
    def _cost(self, X, y, beta):
        self._n_cached = X.shape[0]
        z = X @ beta
        p = _sigmoid(z)
        eps = 1e-12
        return -np.mean(y.ravel() * np.log(p + eps) + (1 - y.ravel()) * np.log(1 - p + eps))

    def _grad(self, X, y, beta):
        z = X @ beta
        p = _sigmoid(z).reshape(-1, 1)
        return (X.T @ (p - y)).ravel() / X.shape[0]

    def predict_proba(self, X):
        return _sigmoid(X @ self.beta_)

    def predict(self, X, threshold=0.5):
        return (self.predict_proba(X) >= threshold).astype(int)


if __name__ == "__main__":
    np.random.seed(0)

    # Linear Regression Demo
    X_lin, y_lin, beta_lin_true = generate_linear_data(sigma=0.3, n=200, m=3)
    lin_model = LinearRegressionGD(lr=0.05, max_iter=2000, tol=1e-8)
    lin_model.fit(X_lin, y_lin)
    mse = np.mean((lin_model.predict(X_lin) - y_lin.ravel()) ** 2)
    print("\n[Linear Regression]")
    print("True β:", beta_lin_true)
    print("Learned β:", lin_model.beta_)
    print(f"Train MSE: {mse:.4f}")

    # Logistic Regression Demo
    X_log, y_log, beta_log_true = generate_logistic_data(theta=0.1, n=300, m=3)
    log_model = LogisticRegressionGD(lr=0.1, max_iter=2000, tol=1e-7)
    log_model.fit(X_log, y_log)
    preds = log_model.predict(X_log)
    acc = (preds.reshape(-1, 1) == y_log).mean()
    print("\n[Logistic Regression]")
    print("True β:", beta_log_true)
    print("Learned β:", log_model.beta_)
    print(f"Train Accuracy: {acc:.3f}; Final Loss: {log_model.cost_history_[-1]:.4f}")
