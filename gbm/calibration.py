import numpy as np
import pandas as pd
import yfinance as yf

def calibrate_from_ticker(ticker: str, period: str = '2y'):
    """Estimate µ and σ from historical price data."""
    df = yf.download(ticker, period=period, progress=False)
    # Handle both flat and MultiIndex columns from yfinance
    if isinstance(df.columns, pd.MultiIndex):
        if ticker in df.columns.levels[1]:
            df = df.xs(ticker, axis=1, level=1)
        elif ticker in df.columns.levels[0]:
            df = df[ticker]
        else:
            try:
                df = df.droplevel(0, axis=1)
            except Exception:
                pass

    price_col = 'Adj Close' if 'Adj Close' in df.columns else 'Close'
    prices = df[price_col].dropna()

    log_returns = np.log(prices / prices.shift(1)).dropna()

    # Annualise (252 trading days)
    mu_daily = log_returns.mean()
    sigma_daily = log_returns.std()

    mu = mu_daily * 252 + 0.5 * (sigma_daily**2) * 252  # Add back Itô correction
    sigma = sigma_daily * np.sqrt(252)

    return {
        'ticker': ticker,
        'S0': float(prices.values[-1]),
        'mu': round(mu, 4),
        'sigma': round(sigma, 4),
        'n_obs': len(log_returns)
    }