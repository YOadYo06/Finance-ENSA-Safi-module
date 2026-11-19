import math
import numpy as np

def simulate_and_price(S0=100, K=100, T=1.0, r=0.05, sigma=0.2, n_steps=252, n_sims=20000, seed=42):
    rng = np.random.default_rng(seed)
    dt = T / n_steps
    Z = rng.standard_normal((n_sims, n_steps))
    increments = (r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z
    S = np.exp(np.log(S0) + np.cumsum(increments, axis=1))
    X = np.exp(-r * T) * np.maximum(S.mean(axis=1) - K, 0.0)
    price = X.mean()
    se = X.std(ddof=1) / math.sqrt(n_sims)
    return price, se

def test_reproducibility_seed():
    p1, _ = simulate_and_price(seed=42)
    p2, _ = simulate_and_price(seed=42)
    assert abs(p1 - p2) < 1e-12

def test_price_non_negative_and_reasonable():
    price, se = simulate_and_price()
    assert price >= 0.0
    assert se >= 0.0
    assert price < 50.0  # borne grossière pour paramètres de test

def test_se_decreases_with_more_sims():
    _, se1 = simulate_and_price(n_sims=5000, seed=1)
    _, se2 = simulate_and_price(n_sims=40000, seed=1)
    assert se2 < se1
