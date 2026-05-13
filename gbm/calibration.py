import numpy as np
import yfinance as yf

def calibrate_from_ticker(ticker: str, period: str = '2y'):
    """Estimate µ and σ from historical price data."""
    df = yf.download(ticker, period=period, progress=False)
    prices = df['Adj Close'].dropna()

    log_returns = np.log(prices / prices.shift(1)).dropna()

    # Annualise (252 trading days)
    mu_daily = log_returns.mean()
    sigma_daily = log_returns.std()

    mu = mu_daily * 252 + 0.5 * (sigma_daily**2) * 252  # Add back Itô correction
    sigma = sigma_daily * np.sqrt(252)

    return {
        'ticker': ticker,
        'S0': float(prices.iloc[-1]),
        'mu': round(mu, 4),
        'sigma': round(sigma, 4),
        'n_obs': len(log_returns)
    }