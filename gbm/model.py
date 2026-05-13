import numpy as np
import matplotlib.pyplot as plt

class GeometricBrownianMotion:
    """
    dS = µS dt + σS dW
    Exact solution: S(t) = S0 * exp((µ - σ²/2)t + σW(t))
    """

    def __init__(self, S0: float, mu: float, sigma: float):
        self.S0 = S0      # Initial price
        self.mu = mu      # Drift (annualised)
        self.sigma = sigma  # Volatility (annualised)

    def simulate(self, T: float, dt: float, n_paths: int = 1, seed: int = None):
        """
        Simulate GBM paths.
        T     : time horizon in years
        dt    : time step (e.g. 1/252 for daily)
        """
        if seed is not None:
            np.random.seed(seed)

        n_steps = int(T / dt)
        t = np.linspace(0, T, n_steps + 1)

        # Standard Brownian increments
        dW = np.random.normal(0, np.sqrt(dt), (n_paths, n_steps))

        # Log-return increments
        log_returns = (self.mu - 0.5 * self.sigma**2) * dt + self.sigma * dW

        # Cumulative sum → price paths
        log_paths = np.hstack([
            np.zeros((n_paths, 1)),
            np.cumsum(log_returns, axis=1)
        ])
        paths = self.S0 * np.exp(log_paths)

        return t, paths

    def plot(self, T=1.0, dt=1/252, n_paths=50, seed=42):
        t, paths = self.simulate(T, dt, n_paths, seed)
        plt.figure(figsize=(12, 5))
        plt.plot(t, paths.T, alpha=0.4, linewidth=0.8)
        plt.plot(t, self.S0 * np.exp(self.mu * t), 'k--', label='Expected path')
        plt.title(f'GBM Simulation  |  µ={self.mu}  σ={self.sigma}  S₀={self.S0}')
        plt.xlabel('Time (years)')
        plt.ylabel('Price')
        plt.legend()
        plt.tight_layout()
        plt.show()