import numpy as np
from scipy.stats import norm
from .model import GeometricBrownianMotion

def black_scholes(S, K, T, r, sigma, option_type='call'):
    """Closed-form Black-Scholes price."""
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    if option_type == 'call':
        return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    else:
        return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

def monte_carlo_price(S0, K, T, r, sigma, n_paths=100_000, option_type='call', seed=42):
    """Monte Carlo option pricing via GBM."""
    gbm = GeometricBrownianMotion(S0=S0, mu=r, sigma=sigma)
    _, paths = gbm.simulate(T=T, dt=T/252, n_paths=n_paths, seed=seed)

    S_T = paths[:, -1]  # Terminal prices

    if option_type == 'call':
        payoffs = np.maximum(S_T - K, 0)
    else:
        payoffs = np.maximum(K - S_T, 0)

    price = np.exp(-r * T) * np.mean(payoffs)
    std_err = np.exp(-r * T) * np.std(payoffs) / np.sqrt(n_paths)
    return price, std_err

def delta(S, K, T, r, sigma, option_type='call'):
    """Black-Scholes Delta."""
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    if option_type == 'call':
        return norm.cdf(d1)
    else:
        return norm.cdf(d1) - 1

def gamma(S, K, T, r, sigma):
    """Black-Scholes Gamma (same for call and put)."""
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    return norm.pdf(d1) / (S * sigma * np.sqrt(T))

def vega(S, K, T, r, sigma):
    """Black-Scholes Vega (same for call and put)."""
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    return S * np.sqrt(T) * norm.pdf(d1)

def theta(S, K, T, r, sigma, option_type='call'):
    """Black-Scholes Theta."""
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    term1 = - (S * sigma * norm.pdf(d1)) / (2 * np.sqrt(T))
    term2 = r * K * np.exp(-r * T)
    if option_type == 'call':
        return term1 - term2 * norm.cdf(d2)
    else:
        return term1 + term2 * norm.cdf(-d2)