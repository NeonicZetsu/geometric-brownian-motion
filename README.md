# geometric-brownian-motion

## Overview
GBM implementation with Monte Carlo option pricing and 
live calibration from Yahoo Finance data.

## Theory
dS = µS dt + σS dW_t

## Features
- [x] Exact GBM path simulation
- [x] Black-Scholes closed-form pricing
- [x] Monte Carlo with confidence intervals
- [x] Greeks (Delta, Gamma, Vega, Theta)
- [x] Historical volatility calibration
- [x] Jupyter notebooks with visualisations

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```python
from gbm import GeometricBrownianMotion, black_scholes, monte_carlo_price, calibrate_from_ticker, delta, gamma, vega, theta

# Calibrate from historical data
params = calibrate_from_ticker('AAPL')
gbm = GeometricBrownianMotion(**params)

# Simulate paths
gbm.plot()

# Price options
bs_price = black_scholes(S=100, K=100, T=1, r=0.05, sigma=0.2)
mc_price, std_err = monte_carlo_price(S0=100, K=100, T=1, r=0.05, sigma=0.2)

# Calculate Greeks
d = delta(S=100, K=100, T=1, r=0.05, sigma=0.2)
```

See [notebooks/gbm_demo.ipynb](notebooks/gbm_demo.ipynb) for a complete example with visualizations.

## Notebooks
- `notebooks/gbm_demo.ipynb` — GBM path simulation, calibration, option pricing, and Greeks.
- `notebooks/greek_readme_demo.ipynb` — notebook documentation demo showing Greek letters, LaTeX math, and README embedding.

GitHub can render notebooks directly when you browse them, and you can link from `README.md` like this:

```markdown
[View the notebook](notebooks/greek_readme_demo.ipynb)
```

For a richer preview, use nbviewer:

```markdown
[View notebook on nbviewer](https://nbviewer.org/github/<your-username>/<your-repo>/blob/main/notebooks/greek_readme_demo.ipynb)
```

Replace `<your-username>` and `<your-repo>` with your GitHub details.

## Results
[Include charts of simulated paths and convergence plots]