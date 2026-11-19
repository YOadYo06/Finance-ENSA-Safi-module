"""Prototype S2 - Monte-Carlo pour options asiatiques (arithmétiques).
À compléter/exécuter via notebook S2, puis factoriser pour Odoo en S3/S5.
"""
import numpy as np

def simulate_gbm_paths(S0, T, r, sigma, n_steps, n_sims, seed=42):
    rng = np.random.default_rng(seed)
    dt = T / n_steps
    Z = rng.standard_normal((n_sims, n_steps))
    increments = (r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z
    log_paths = np.log(S0) + np.cumsum(increments, axis=1)
    S = np.exp(log_paths)
    return S

def price_asian_call_mc(S0, K, T, r, sigma, n_steps=252, n_sims=100_000, seed=42):
    S = simulate_gbm_paths(S0, T, r, sigma, n_steps, n_sims, seed)
    A = S.mean(axis=1)
    payoffs = np.maximum(A - K, 0.0)
    X = np.exp(-r * T) * payoffs
    price = X.mean()
    std = X.std(ddof=1)
    se = std / np.sqrt(n_sims)
    ci_low = price - 1.96 * se
    ci_high = price + 1.96 * se
    return {
        "price": float(price),
        "std": float(std),
        "se": float(se),
        "ci_low": float(ci_low),
        "ci_high": float(ci_high),
    }

if __name__ == "__main__":
    res = price_asian_call_mc(S0=100, K=100, T=1.0, r=0.05, sigma=0.2, n_steps=252, n_sims=10000)
    print(res)
