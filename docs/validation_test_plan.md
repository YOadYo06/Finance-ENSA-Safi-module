# Plan de validation, tests & reproductibilité — Semaine 1 (Projet 5)

## 1. Objectifs de validation (Projet 5)
- Vérifier la **cohérence** du prix Monte-Carlo et de l’intervalle de confiance à 95 %.
- Mesurer la **réduction de variance** apportée par la variable de contrôle.
- Vérifier la **convergence** : $SE \propto 1/\sqrt{N}$ (pente ≈ −1/2 en log-log de $SE$ vs $N$).

## 2. Réduction de variance (variable de contrôle)
- **Contrôle :** call européen de payoff $Y = e^{-rT}\max(S_T - K, 0)$ avec $E[Y]$ donné par Black-Scholes.
- **Estimateur corrigé :** $X_c = X - \beta (Y - E[Y])$, $\beta^* = \operatorname{Cov}(X,Y)/\operatorname{Var}(Y)$.
- **Métriques à rapporter :**
  - $SE$ avant vs après contrôle, ratio $SE/SE_c$.
  - Corrélation $\rho(X,Y)$ et gain théorique attendu $(1-\rho^2)$ sur la variance.
  - (Bonus) variables antithétiques ($Z$ et $-Z$), contrôle par asiatique géométrique.

## 3. Tests de convergence
- Tracer $SE(N)$ pour $N \in \{10^3, 10^4, 10^5, 10^6\}$ (ou sous-ensemble selon temps de calcul).
- Vérifier visuellement/en régression log-log la pente ≈ −0.5.
- Comparer stabilité des résultats avec graine fixée vs non fixée.

## 4. Reproductibilité
- **Graine fixée :** `numpy.random.default_rng(42)` (documentée dans `docs/data_source.md`).
- Jeux de paramètres de référence (sanity checks), ex. $S_0=100, K=100, T=1, r=0.05, \sigma=0.2, n=252$.
- Enregistrer les sorties attendues (prix/IC approximatifs) pour non-régression.

## 5. Stratégie de tests (pytest, à partir de S5)
- `tests/test_mc_asian.py` : prix MC dans des bornes raisonnables, IC contient l’estimation, $SE$ décroît quand $N$ augmente.
- `tests/test_control_variate.py` : $SE_c \le SE$ (en général), estimateur corrigé non biaisé (moyenne proche).
- `tests/test_reproducibility.py` : même graine + mêmes paramètres ⇒ mêmes résultats.
- `tests/test_barrier.py` (extension) : payoff knock-out ≤ payoff sans barrière.

## 6. Référence simple
- Black-Scholes (européen) comme contrôle/valeur de référence analytique.
- Cas limites : $\sigma \to 0$, $T \to 0$ (sanity checks) si temps disponible.

## 7. Statut S1
- [x] Plan de validation et métriques définis.
- [x] Squelette de tests préparé (`tests/`) pour commits ultérieurs.
- [ ] Implémentation des tests (S5) et exécution CI/manuelle (S5–S6).
