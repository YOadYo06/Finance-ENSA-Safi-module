# Source des données et paramètres — Semaine 1 (Projet 5)

## 1. Type de données
Le Projet 5 ne requiert pas obligatoirement de données de marché propriétaires : les simulations Monte-Carlo fonctionnent à partir de **paramètres** saisis ou estimés.

## 2. Paramètres retenus (à saisir dans `cours.montecarlo`)
| Paramètre | Symbole | Exemple / convention | Source |
|---|---|---|---|
| Prix initial | $S_0$ | ex. 100 (ou dernier cours) | Saisie utilisateur / `yfinance` (close) |
| Strike | $K$ | ex. 100 | Saisie utilisateur |
| Maturité | $T$ | en années (ex. 1.0) | Saisie utilisateur (convention annualisée) |
| Taux sans risque | $r$ | ex. 0.03 (3%) | Hypothèse / saisie (constant) |
| Volatilité | $\sigma$ | ex. 0.20 (20%) | Volatilité historique via `yfinance` **ou** saisie |
| Dates de fixing | $n$ | ex. 252 | Saisie (surveillance discrète) |
| Simulations | $N$ | 10 000 à 1 000 000 | Saisie (compromis précision/temps) |
| Barrière | $H$ | si option barrière | Saisie utilisateur |
| Graine | seed | 42 | Fixée pour reproductibilité |

## 3. Source optionnelle (volatilité historique)
- **Bibliothèque :** `yfinance` (données publiques Yahoo Finance) pour récupérer une série de prix et estimer $\sigma$ historique annualisée.
- **Exemple de ticker (à adapter) :** `AAPL`, `MSFT` ou un actif de la Bourse de Casablanca si disponible via une source équivalente ; à défaut, paramètres de démonstration saisis manuellement.
- **Lien/outils :** https://pypi.org/project/yfinance/ (à confirmer selon environnement du groupe).

## 4. Conventions communes (à respecter dans le groupe/projets liés)
- $T$ en années, taux/vol annualisés.
- Reproductibilité : `numpy.random.default_rng(seed)` avec graine documentée (ex. 42).
- Format de données d’entrée : champs du modèle `cours.montecarlo` (Odoo) et/ou dict/DataFrame en notebook.

## 5. Statut S1
- [x] Source/approche choisie : paramètres saisis + volatilité historique optionnelle via `yfinance`.
- [x] Conventions documentées pour le prototype S2 et l’intégration S3.
