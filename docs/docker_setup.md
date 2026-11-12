# Docker — Installation & validation (Semaine 1)

> **Exigence S1 :** Docker installé dès la semaine 1, en partant du TP 0 / module `cours_derives`.

## 1. Installation (poste de chaque membre)
- **Windows :** installer [Docker Desktop](https://www.docker.com/products/docker-desktop/) (WSL2 recommandé), activer la virtualisation si nécessaire.
- **Linux :** installer Docker Engine + Docker Compose plugin (`docker compose version`).
- Vérifier l’installation :
  ```bash
  docker --version
  docker compose version
  docker run --rm hello-world
  ```

## 2. Mise en place avec le TP 0 / `cours_derives`
1. Récupérer le code du TP 0 / module `cours_derives` (base fournie en cours) dans l’environnement du groupe.
2. Utiliser le `docker-compose.yml` du TP 0 (Odoo + PostgreSQL) ou celui du dépôt si présent.
3. Démarrer les services :
   ```bash
   docker compose up -d
   ```
4. Accéder à Odoo (URL/port selon configuration TP 0, ex. `http://localhost:8069`), installer/mettre à jour le module `cours_derives`.
5. Confirmer que l’ajout du futur modèle `cours.montecarlo` (S3) pourra se faire dans ce module.

## 3. Validation S1 (à montrer en mini-compte rendu)
- [ ] `docker --version` et `docker compose version` OK sur les postes
- [ ] Conteneurs TP 0 démarrés (`docker compose ps`)
- [ ] Odoo accessible et module `cours_derives` chargé
- [ ] Preuve/capture ou note de validation ajoutée par le Développeur Odoo (commit S1)

## 4. Remarques
- Ne pas committer de secrets/mots de passe ; utiliser `.env` si nécessaire (et `.gitignore`).
- En cas de problème Windows/WSL2, documenter la solution dans ce fichier lors du commit du Dév. Odoo.
