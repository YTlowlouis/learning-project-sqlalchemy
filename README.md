# learning-project-sqlalchemy
🧠 Projet : Mini-ORM Social Network (SQLAlchemy)
📌 Objectif

Créer un backend Python utilisant SQLAlchemy pour gérer un mini réseau social, avec :

Utilisateurs
Posts
Commentaires
Likes
Relations (followers)
⚙️ Contraintes générales
Python 3.10+
Utilisation de SQLAlchemy (ORM obligatoire, Core en bonus)
Base de données : SQLite (obligatoire), PostgreSQL (bonus)
Pas de framework web (Flask/FastAPI en bonus seulement)
Code propre (PEP8, modularisation)
Migrations avec Alembic (obligatoire)
🏗️ Partie 1 — Modélisation (Base ORM)

Créer les modèles suivants :

User
id
username (unique)
email (unique)
created_at
Post
id
content
created_at
user_id
Comment
id
content
created_at
user_id
post_id
Like
id
user_id
post_id
Follow (self-relation)
follower_id
followed_id

👉 Concepts SQLAlchemy appris :

Declarative Base
Relationships (relationship, back_populates)
Foreign keys
Many-to-many (followers)
Index & contraintes
🔄 Partie 2 — CRUD avancé

Implémente :

Users
Créer un utilisateur
Récupérer un utilisateur par username
Supprimer un utilisateur
Posts
Créer un post
Récupérer tous les posts d’un utilisateur
Supprimer un post
Comments
Ajouter un commentaire à un post
Likes
Like / Unlike un post

👉 Concepts appris :

Session lifecycle
Transactions
Flush vs Commit
Query ORM
🔍 Partie 3 — Requêtes complexes

Implémente ces requêtes :

Top 5 posts les plus likés
Nombre de followers par utilisateur
Posts d’un utilisateur + nombre de commentaires
Feed d’un utilisateur (posts des gens suivis)
Utilisateurs sans posts

👉 Concepts appris :

join, outerjoin
group_by
func.count
Subqueries
Aliases
⚡ Partie 4 — Performance & optimisation

Optimise les requêtes :

Évite le N+1 problem
Utilise :
joinedload
selectinload
Ajoute des index pertinents

👉 Concepts appris :

Lazy vs Eager loading
Optimisation ORM
🧱 Partie 5 — SQLAlchemy Core (important 42 mindset)

Refais certaines requêtes sans ORM :

Insert utilisateur
Requête top posts
Feed utilisateur

👉 Concepts :

select()
insert()
update()
connection.execute()
🔐 Partie 6 — Transactions & erreurs

Implémente :

Rollback en cas d’erreur
Gestion des conflits (username déjà pris)
Transactions imbriquées

👉 Concepts :

session.rollback()
try/except
Atomicité
🧪 Partie 7 — Tests
Tests unitaires (pytest recommandé)
Base de données de test
Fixtures
