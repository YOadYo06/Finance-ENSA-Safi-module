# S1 — Outline algorithme Monte-Carlo (Projet 5)

Préparation S2 : prototype notebook pour la valorisation d’options asiatiques (et extension barrière).

## Étapes à implémenter
1. **Entrées** : `S0, K, T, r, sigma, n, N, seed`, `option_type`, `barriere?`
2. **Trajectoires GBM (sous Q)** :
   - `dt = T/n`
   - `Z = rng.standard_normal((N, n))`
   - `logS = log(S0) + cumsum((r - 0.5*sigma**2)*dt + sigma*sqrt(dt)*Z, axis=1)`
   - `S = exp(logS)` (inclure ou gérer `S0` selon convention)
3. **Payoff asiatique arithmétique (call)** : `A = S.mean(axis=1)` ; `payoff = maximum(A - K, 0)`
4. **Actualisation & estimateur** : `X = exp(-r*T)*payoff` ; `prix = X.mean()` ; `s = X.std(ddof=1)` ; `SE = s/sqrt(N)` ; IC95 = `[prix ± 1.96*SE]`
5. **Extension barrière knock-out** : annuler payoff si `S.max(axis=1) >= H` (up-and-out) ou selon type.
6. **Variable de contrôle** :
   - `Y = exp(-r*T)*maximum(S[:, -1] - K, 0)` (call européen)
   - `EY = bs_call(S0,K,T,r,sigma)` (Black-Scholes analytique)
   - `beta = cov(X,Y)[0,1]/var(Y)` ; `Xc = X - beta*(Y - EY)` ; prix/SE corrigés
7. **Convergence** : boucle sur plusieurs `N`, tracer `SE(N)` en log-log (pente cible −1/2).

## Livrables S2
- Notebook exécutable (prix + IC + contrôle de variance + graphiques).
- Fonctions réutilisables pour intégration Odoo (`action_simuler`) en S3/S5.
