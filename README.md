# Projet de "Base de Données 1" : Compilation SPJRUD vers SQL

## Introduction

Ce projet est rendu dans le cadre du cours "Bases de données 1" dispensé par le Prof. Sébastien Bonte en année académique 2020-2021. Il consiste à créer une application en python permettant de compiler des requêtes SPJRUD vers des requêtes SQL. De plus, cette application doit vérifier que la requête SPJRUD est initialement correcte.

## Choix d'implémentation

### Packages

Les classes sont séparer en 3 packages différent :

- Le package 'comparison' contient toutes les classes nécessaires au comparaison (par exemple pour la requête "select"), c'est-à-dire les classes représentant "=", ">", ...
- Le package 'relations' contient toutes les classes représentant des requêtes/relations (exemple : "Select", "Join", ...)
- Le package 'system' contient toutes les classes nécessaire au bon fonctionnement du système (autre que "Main") telles que le lien avec la base de données.

### Package 'comparison'

coming soon...

### Package 'relations'

J'ai choisi de représenter chaque requête avec une classe portant de le nom de la requête. Chacune de celles-ci héritent d'une classe "Rel" qui représente une relation. En effet, chaque requête, une fois executée, correspond elle aussi à une relation.

De plus, chaque requête prend en paramètres une ou des relations qui peuvent donc soit être :

- un objet "Rel" si la relation est une table en base de données.
- Une des classe représentant une requête si cette dernière s'effectue elle même sur une autre relation. 

Tout ensemble de requête contient, dès lors, au minimun un objet "Rel".

### Package 'system'

Coming soon...

## Fonctionnalités supplémentaires

Coming soon...

## Difficultés rencontrées/Solutions apportées

Au début, j'envisageais d'effectuer recursivement chaque requétes en appelant la méthode "execute" de chaque requête passée en paramètre. Cette méthode ne prenait en compte que le schema de base de données de la relation. Cela fonctionnait parfaitement au premier abord, mais lorsque j'ai voulu implémenter la requête "rename", un problème m'a forcé à changer mon architecture.

En effet, la requéte "rename" en sql s'effectue sur une table de la base de données. Or, la méthode "execute" recursive s'effectue uniquement sur le schema de base de données sans avoir une table dans le fichier "database.db". J'ai donc considéré une seconde approche. Toute requête crée une table en base de données qui correspond à la requête demandée. Elle s'effectue donc sur la table de la requête effectué précédemment et en crée une nouvelle. Ensuite elle supprime la table de la requête précédente, affiche le résultat de la table, et supprime la table de la requête actuelle si et seulement si c'est la dernière requête à effectuer.

## Documentation

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
