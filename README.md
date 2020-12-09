# Projet de "Base de Données 1" : Compilation SPJRUD vers SQL

## Introduction

Ce projet est rendu dans le cadre du cours "Bases de données 1" dispensé par le Prof. Sébastien Bonte en année académique 2020-2021. Il consiste à créer une application en python permettant de compiler des requêtes SPJRUD vers des requêtes SQL. De plus, cette application doit vérifier que la requête SPJRUD est initialement correcte.

## Choix d'implémentation

### Packages

Les classes sont séparée en 3 packages différent :

- Le package 'comparison' contient toutes les classes nécessaires au comparaison (par exemple pour la requête "select"), c'est-à-dire les classes représentant "=", ">", ...
- Le package 'relations' contient toutes les classes représentant des requêtes/relations (exemple : "Select", "Join", ...)
- Le package 'system' contient toutes les classes nécessaire au bon fonctionnement du système (autre que "Main") telles que le lien avec la base de données.

#### Package 'comparison'

J'ai choisi de créer une classe globale qui représente une égalité. Ensuite, toutes les autres comparaisons comme le "plus grand" et le "plus petit" hérite de cette classe globale. En effet, la seule différence entre ces comparaisons et la classe d'égalité est l'opérateur utilisé lors de la comparaison.

#### Package 'relations'

J'ai choisi de représenter chaque requête avec une classe portant de le nom de la requête. Chacune de celles-ci héritent d'une classe "Rel" qui représente une relation. En effet, chaque requête, une fois executée, correspond elle aussi à une relation.

De plus, chaque requête prend en paramètres une ou des relations qui peuvent donc soit être :

- un objet "Rel" si la relation est une table en base de données.
- Une des classe représentant une requête si cette dernière s'effectue elle même sur une autre relation. 

Tout ensemble de requête contient, dès lors, au minimun un objet "Rel".

#### Package 'system'

J'ai implementé la classe 'SqlLiteDatabase' grâce au design pattern Singleton. Celui-ci a été utilisé dans un soucis de concision. En effet, cela a permis de ne pas devoir passer en paramètres cet objet dans chaque objet représentant une requête. De plus, cela permet de facilement voir à quelle base de données appartient une requête en regardant les requêtes comprises entre la création de l'object 'SqlLiteDatabase' et l'appel à la méthode "close()".

Pour afficher une table à la console, j'ai pris la décision de créer une classe à part 'Displayer'. Cela permet de bien distinguer clairement la partie logique de l'affichage à la console.

### Execution des requêtes

Chaque requête, lors de son execution, transforme la requête en une requête SQL. Ensuite, elle l'execute sur la base de données associée à la requête et, dès lors, une table est créée en base de données. Cette méthode a été utilisée pour chaque requête utilise la table créée précedemment, crée une nouvelle table en base de données, et supprime par la suite la table de la requête précédente (sauf si cette table est la table originelle).

Cette architecture a été utilisée après avoir rencontré un problème au cours de l'implémentation (voir section "Difficultés rencontrées/Solutions apportées")

## Fonctionnalités supplémentaires

Coming soon...

## Difficultés rencontrées/Solutions apportées

Au début, j'envisageais d'effectuer recursivement chaque requétes en appelant la méthode "execute" de chaque requête passée en paramètre. Cette méthode ne prenait en compte que le schema de base de données de la relation. Cela fonctionnait parfaitement au premier abord, mais lorsque j'ai voulu implémenter la requête "rename", un problème m'a forcé à changer mon architecture.

En effet, la requéte "rename" en sql s'effectue sur une table de la base de données. Or, la méthode "execute" recursive s'effectue uniquement sur le schema de base de données sans avoir une table dans le fichier "database.db". J'ai donc considéré une seconde approche. Toute requête crée une table en base de données qui correspond à la requête demandée. Elle s'effectue donc sur la table de la requête effectué précédemment et en crée une nouvelle. Ensuite elle supprime la table de la requête précédente.

## Documentation

### Utilisation de la librairie

Pour pouvoir utiliser ce module, il faut d'abord l'importer :

> from spjrud_converter import *

Comme les requêtes doivent être executées sur une base de données SQLite, il faut ensuite créer un objet 'SqlLiteDatabase' qui prend en paramètre le nom de la base de données (le chemin du fichier .db)

> db = SqlLiteDatabase('database.db')

Remarque : une seul objet 'SqlLiteDatabase' peut être actif à la fois (voir la section "Choix d'implémentation" pour la justification de ce choix).

### Objet 'SqlLiteDatabase'

> db.reset()

Cette méthode permet d'effacer toutes les tables de la base de données.

Celle-ci peut également prendre une liste en paramètres permettant de spécifier les tables de la base de données à conserver.

> db.reset(['countries', 'lands', 'r', 's'])

---

> db.execute()

Cette méthode permet d'executer une requête SPJRUD passée en paramètres (voir la section suivante pour les différentes requêtes). Elle affiche également le résultat de la requête dans la console.

---

> db.commit()

Cette méthode permet de garder les changements en base de données.

> db.rollback()

Cette méthode, inversément à la méthode "commit()" ci dessus, permet d'enlever les changements en base de données depuis le dernier commit.

---

> db.close()

Cette méthode met fin à la connexion avec la base de données.

---

> db.getTables()

Cette méthode retourne toutes les tables contenues en base de données.

---

> db.getTable(table_name)

Cette méthode retourne toutes les données contenues dans une table de la base de données. Le paramètres 'table_name' représente le nom de la table dans la base de données.

### Requêtes SPJRUD

---

> Select(comparaison, relation)

- comparaison : condition de sélection (égalité, inégalité, ...)
- relation : la relation sur laquelle effectué la selection

---

> Projection(liste_attributs, relation)

- liste_attributs : tous les attributs que l'on veut récupérer avec la sélection
- relation : la relation sur laquelle effectué la projection

---

> Rename(attribut, nouveau_nom, relation)

- attribut : l'attribut à renommer
- nouveau_nom : le nouveau nom à donner à l'attribut
- relation : la relation sur laquelle effectué le renommage

---

> Join(relation_1, relation_2)

- relation_1 : la première relation sur laquelle effectué la jointure
- relation_2 : la seconde relation sur laquelle effectué la jointure

---

> Union(relation_1, relation_2)

- relation_1 : la première relation sur laquelle effectué la jointure
- relation_2 : la seconde relation sur laquelle effectué la jointure

---

> Diff(relation_1, relation_2)

- relation_1 : la première relation sur laquelle effectué la jointure
- relation_2 : la seconde relation sur laquelle effectué la jointure

## Remarques éventuelles

Coming soon...
