# Plan de push — Semaine 1 (Projet 5)

**Règles (PDF):** 1 commit/semaine/étudiant minimum, message avec nom ou initiales (ex. `[Youness] ...`). Pas de push groupé par une seule personne pour tout le contenu.

Attribuez les rôles S1–S4 dans l'équipe, puis chaque membre pousse les fichiers de sa responsabilité (vous pouvez adapter la répartition). Suggestion par rôle :

## 1. Chef de Projet / Finance
- **Fichiers à pousser :** `README.md`, `docs/fiche_lecture_projet5.md` (coordination/rédaction), `docs/gantt_previsionnel.md`, `docs/PUSH_PLAN_S1.md` (si ajusté)
- **Exemples de commits :**
  - `[Nom] S1: ajout README et cadrage projet 5`
  - `[Nom] S1: fiche de lecture Phase 0 (formules, hypothèses, lien TP0)`
  - `[Nom] S1: dépôt du Gantt prévisionnel et rotation S4`

## 2. Quant / Data (Python)
- **Fichiers à pousser :** `docs/data_source.md`, `notebooks/00_s1_algo_outline.md` (ou notebook squelette)
- **Exemples de commits :**
  - `[Nom] S1: choix source données/paramètres et graine reproductibilité`
  - `[Nom] S1: squelette notebook et étapes algorithme Monte-Carlo`

## 3. Développeur Odoo (ERP)
- **Fichiers à pousser :** `docs/docker_setup.md`, `docs/schema_bdd.md`
- **Exemples de commits :**
  - `[Nom] S1: guide Docker et validation environnement TP0`
  - `[Nom] S1: schéma BDD extension cours_derives (cours.montecarlo)`

## 4. Ingénieur IA / Testeur
- **Fichiers à pousser :** `docs/validation_test_plan.md`, `tests/.gitkeep` ou squelette `tests/test_placeholder.py`
- **Exemples de commits :**
  - `[Nom] S1: plan de validation, réduction de variance et convergence`
  - `[Nom] S1: squelette tests pytest et conventions reproductibilité`

## Ordre suggéré
1. Créer une branche courte par fonctionnalité (ex. `s1-fiche-lecture`, `s1-schema-bdd`) ou travailler proprement sur `main` selon accord du groupe.
2. Chaque membre fait son commit local puis `git push` de **sa** branche/commit.
3. Relecture croisée (pull requests) recommandée par le PDF.

## Vérification S1 avant mini-compte rendu
- [ ] Chaque membre apparaît dans `git log` (S1)
- [ ] `docs/` contient fiche, schéma, Gantt, data source
- [ ] Docker installé et testé par l'équipe
- [ ] Gantt prévisionnel inclut jalons S1–S7 et rotation fin S4
