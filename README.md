# locationDeVoiture_Django

Voici les étapes générales pour créer un projet de location de voitures en utilisant le framework Django :

    	Installer Django : Vous devez d'abord installer Django sur votre système si ce n'est pas déjà fait. Vous pouvez installer Django en utilisant pip, qui est un outil de gestion des packages Python. 
	Pour installer Django, ouvrez une console et exécutez la commande suivante :

								pip install Django

		- Créer un projet Django : Après avoir installé Django, vous pouvez créer un nouveau projet Django en utilisant la commande suivante :

		django-admin startproject nom-du-projet (dans notre cas c'etait nomé 'location_de_voiture')

Cela créera un nouveau répertoire avec le nom que vous avez spécifié. Vous pouvez naviguer dans ce répertoire pour commencer à travailler sur votre projet.

		- Configurer la base de données : Vous devez configurer la base de données pour votre projet. Django prend en charge de nombreux types de bases de données, notamment PostgreSQL, MySQL et SQLite. 
		Vous pouvez configurer la base de données dans le fichier settings.py de votre projet. (Le type que nous avions choisis c'est MySQL), pour que les entitées soient creer, nous avons
		besoins de suivre les etapes suivantes:
			--- Creer une nouvelle base de données en phpMyAdmin avec le meme nom mentioné dans le projet (settings.py dans le champs DATABASES { ... NAME : ...} )
			--- Utiliser la commande 			python manage.py makemigrations : 	permet de générer des fichiers de migration pour les changements que vous avez apportés à vos modèles Django.

			--- Utiliser la commande 			python manage.py makemigrations app :	permet de générer des fichiers de migration uniquement pour l'application spécifiée.

			--- Utiliser la commande 			python manage.py migrate app	:	applique les fichiers de migration à la base de données pour l'application spécifiée.

			--- Utiliser la commande 			python manage.py migrate	:	vérifie les fichiers de migration en attente pour chaque application de votre projet, puis exécute les instructions SQL
														nécessaires pour mettre à jour la structure de la base de données. Cela peut inclure la création de nouvelles tables ou colonnes,
														la modification de tables ou colonnes existantes, ou la suppression de tables ou colonnes qui ne sont plus nécessaires.			

		- Créer des applications Django : Les applications Django sont des modules réutilisables qui contiennent des fonctionnalités spécifiques. Pour votre projet de location de voitures, vous pouvez créer des applications telles que "clients", "véhicules" et "locations". Pour créer une application, exécutez la commande suivante :

								python manage.py startapp nom-de-l-application

		- Créer des modèles Django : Les modèles Django définissent la structure de vos données. Vous pouvez créer des modèles pour les clients, les véhicules et les locations. Les modèles sont définis dans des fichiers models.py dans chaque application Django.

		- Configurer les vues Django : Les vues Django définissent la logique de votre application. Vous pouvez créer des vues pour afficher les détails des clients, des véhicules et des locations. Les vues sont définies dans des fichiers views.py dans chaque application Django.

		- Configurer les URL Django : Les URL Django permettent de mapper les URLs de votre site web vers les vues correspondantes. Vous pouvez créer des URL pour chaque vue que vous avez créée. Les URL sont définies dans des fichiers urls.py dans chaque application Django.

		- Créer des templates Django : Les templates Django sont des fichiers HTML qui définissent la présentation de votre application. Vous pouvez créer des templates pour afficher les détails des clients, des véhicules et des locations. Les templates sont stockés dans un répertoire templates dans chaque application Django.

		- Lancer le serveur de développement : Vous pouvez lancer le serveur de développement Django en exécutant la commande suivante :

   								 python manage.py runserver

    	Cela lancera un serveur web local qui vous permettra de voir votre application en action. Vous pouvez accéder à votre application en ouvrant votre navigateur web et en visitant l'URL http://localhost:8000/.

	Voilà, vous avez maintenant une base solide pour commencer à développer votre projet de location de voitures en Django !
