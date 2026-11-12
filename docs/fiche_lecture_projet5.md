# Fiche de lecture — Phase 0 (Semaine 1)
**Projet 5 : Monte-Carlo pour Options Exotiques**  
**Groupe 5 :** LAHLALI Abdelhaq, KHALLOUK Abderrahmane, MAELAININE Chaibatta, ADIL Youness

## 1. Formules clés (recopiées et expliquées)

### 1.1 Dynamique du sous-jacent (GBM sous la probabilité risque-neutre $\mathbb{Q}$)
Schéma exact de discrétisation sur un pas $\Delta t$ :
$$
S_{t+\Delta t} = S_t \exp\left(\left(r - \frac{\sigma^2}{2}\right)\Delta t + \sigma \sqrt{\Delta t}\, Z\right), \qquad Z \sim \mathcal{N}(0,1)
$$
- $S_t$ : prix du sous-jacent, $r$ : taux sans risque, $\sigma$ : volatilité, $\Delta t = T/n$.
- Sous $\mathbb{Q}$ le drift est $r$ (et non le rendement réel), ce qui permet d’actualiser au taux sans risque.

### 1.2 Payoff d’une option asiatique arithmétique (call, surveillance discrète)
Moyenne arithmétique des prix aux dates de fixing $t_1,\dots,t_n$ :
$$
A = \frac{1}{n}\sum_{k=1}^{n} S_{t_k}, \qquad \text{Payoff} = \max(A - K, 0)
$$
(Pour un put asiatique : $\max(K - A, 0)$.) Le payoff dépend du **chemin** (path-dependent), d’où l’intérêt de Monte-Carlo.

### 1.3 Estimateur Monte-Carlo, erreur standard et intervalle de confiance à 95 %
Soit $X_i = e^{-rT}\,\text{Payoff}_i$ le payoff actualisé de la trajectoire $i$ ($i=1,\dots,N$, i.i.d.) :
$$
\hat{P}_N = \frac{1}{N}\sum_{i=1}^{N} X_i, \qquad s = \sqrt{\frac{1}{N-1}\sum_{i=1}^{N}(X_i - \hat{P}_N)^2}
$$
$$
SE = \frac{s}{\sqrt{N}}, \qquad IC_{95\%} = \left[\hat{P}_N - 1{,}96\,SE\;;\; \hat{P}_N + 1{,}96\,SE\right]
$$
- Justification : Loi des Grands Nombres ($\hat{P}_N \to \mathbb{E}[X]$) et Théorème Central Limite (erreur d’ordre $O(1/\sqrt{N})$).

### 1.4 Réduction de variance — variable de contrôle
On utilise une variable $Y$ corrélée à $X$ dont l’espérance $E[Y]$ est connue analytiquement (ici, le prix Black-Scholes d’un call européen) :
$$
X_c = X - \beta\,(Y - E[Y]), \qquad \beta^* = \frac{\operatorname{Cov}(X,Y)}{\operatorname{Var}(Y)}
$$
$$
\operatorname{Var}(X_c) = \operatorname{Var}(X)\,(1 - \rho^2), \qquad \rho = \operatorname{Corr}(X,Y)
$$
- L’estimateur corrigé garde la même espérance mais une variance réduite (gain d’autant plus fort que $|\rho|$ est proche de 1). En pratique $\beta^*$ est estimé empiriquement sur l’échantillon.

### 1.5 Extension — option à barrière (knock-out)
Exemple (up-and-out call) : le payoff est annulé si le sous-jacent franchit la barrière $H$ sur la trajectoire :
$$
\text{Payoff}_{KO} = \mathbf{1}_{\{\max_{k \le n} S_{t_k} < H\}} \cdot \max(S_T - K, 0)
$$
(Variante down-and-out : condition sur $\min S_{t_k} > H$.) La surveillance **discrète** sous-estime la probabilité de franchissement continu.

## 2. Hypothèses de marché
- Sous-jacent log-normal suivant un **GBM** ; taux $r$ et volatilité $\sigma$ **constants**.
- Simulation sous la **probabilité risque-neutre** $\mathbb{Q}$ (drift = $r$).
- Trajectoires **i.i.d.** ; $N$ suffisamment grand pour que le TCL s’applique.
- **Surveillance discrète** aux $n$ dates de fixing (ex. 252) ; pour les barrières, la surveillance discrète sous-estime le franchissement par rapport au continu.
- Pas de coûts de transaction, pas de dividendes (sauf extension), marché sans arbitrage.

## 3. Lien avec le TP 0 / module `cours_derives` (Odoo)
On part du module du TP 0 (`cours_derives`) et on l’étend par un nouveau modèle dédié à la simulation Monte-Carlo :
- **Nouveau modèle `cours.montecarlo`** (dans `cours_derives`) avec les champs :
  - Paramètres/choix : `type` (asiatique / barrière), `S0`, `K`, `T`, `r`, `sigma`, `barriere`, `n_dates`, `n_simulations`.
  - Résultats : `prix_mc`, `ecart_type`, `ic_bas`, `ic_haut`, `prix_cv`, `ecart_type_cv`.
- **Méthode `action_simuler()`** : lance la simulation, calcule le prix Monte-Carlo et l’IC 95 %, calcule la version avec variable de contrôle et renseigne les champs.
- **Vue** : formulaire de saisie + bouton « Simuler » + affichage des résultats et indicateur de réduction de variance (rapport des écarts-types / SE avant vs après contrôle).
- **Réutilisation** : le prix analytique Black-Scholes (ex. Groupe 1 / utilitaire TP 0) sert de variable de contrôle ($E[Y]$) et de référence de comparaison.

## 4. Algorithme de calcul en Python (démarche)
1. **Entrées** : $S_0, K, T, r, \sigma$, type (asiatique/barrière), $n$ dates, $N$ simulations, barrière $H$ si besoin, graine RNG.
2. **Génération des trajectoires** : tirer une matrice $Z \in \mathbb{R}^{N\times n}$ de normales, calculer les log-rendements cumulés (`np.cumsum`) pour obtenir $S_{t_k}$ (schéma GBM exact).
3. **Payoffs** :
   - Asiatique : moyenne arithmétique sur l’axe des dates $\Rightarrow$ payoff $\max(A-K,0)$.
   - Barrière (extension) : appliquer le masque knock-out via $\max/\min$ du chemin vs $H$.
4. **Prix & IC** : actualiser $X_i = e^{-rT}\text{Payoff}_i$, calculer $\hat{P}_N$, $s$, $SE$, $IC_{95\%}$.
5. **Variable de contrôle** : calculer $Y_i$ (payoff actualisé d’un call européen sur $S_T$, corrélé), obtenir $E[Y]$ par Black-Scholes, estimer $\beta^*$ puis $\hat{P}_{c}$ et $SE_c$.
6. **Sorties** : prix, écart-type/SE, bornes IC, prix/SE avec contrôle, indicateur de réduction de variance ; courbe de convergence $SE(N)$ (pente $-1/2$ en log-log) pour le rapport.
7. **Reproductibilité** : fixer `numpy.random.default_rng(seed)` (ex. 42).

## 5. Références (chapitres du polycopié)
- Chapitre 4 : mouvement brownien géométrique, simulation Monte-Carlo, options exotiques (asiatiques/barrières).
- Chapitre 1 (rappel) : valorisation risque-neutre et actualisation, formule de Black-Scholes (utilisée comme contrôle/référence).
