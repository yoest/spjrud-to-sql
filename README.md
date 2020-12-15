# Projet de "Base de Données 1" : Compilation SPJRUD vers SQL

## Introduction

Ce projet est rendu dans le cadre du cours "Bases de données 1" dispensé par le Prof. Sébastien Bonte en année académique 2020-2021. Il consiste à créer une application en python permettant de compiler des requêtes SPJRUD vers des requêtes SQL. De plus, cette application doit vérifier que la requête SPJRUD est initialement correcte.

## Choix d'implémentation

### Packages

Les classes sont séparée en 3 packages différent :

- Le package 'comparison' contient toutes les classes nécessaires au comparaison (par exemple pour la requête "select"), c'est-à-dire les classes représentant "=", ">", ...
- Le package 'relations' contient toutes les classes représentant des requêtes/relations (exemple : "Select", "Join", ...)
- Le package 'system' contient toutes les classes nécessaire au bon fonctionnement du système (autre que "Main") telles que le lien avec la base de données ou l'affichage d'une requête dans la console.

#### Package 'comparison'

Pour représenter des comparaisons, j'ai décidé de créer une classe globale qui représente une égalité. Ensuite, toutes les autres comparaisons, telles que "plus grand" ou "plus petit", héritent de cette classe globale. En effet, la seule différence entre ces comparaisons et la classe d'égalité est l'opérateur utilisé lors de la comparaison.

#### Package 'relations'

Il a été décicé de représenter chaque requête avec une classe portant le nom de la requête. Chacune de celles-ci héritent d'une classe "Rel" qui représente une relation. En effet, chaque requête, une fois executée, correspond elle aussi à une relation.

De plus, chaque requête prend en paramètres une ou des relations qui peuvent donc soit être :

- un objet "Rel" si la relation est une table en base de données (ou éventuellement un schema fourni par l'utilisateur).
- Une des classe représentant une requête si cette dernière s'effectue elle même sur une autre relation.

Tout ensemble de requête contient, dès lors, au minimun un objet "Rel".

#### Package 'system'

J'ai implementé la classe 'SqlLiteDatabase' grâce au design pattern Singleton. Celui-ci a été utilisé dans un soucis de concision. En effet, cela a permis de ne pas devoir passer en paramètres cet objet dans chaque objet représentant une requête. De plus, cela permet de facilement voir à quelle base de données appartient une requête. En effet, il suffit de regarder les requêtes comprises entre la création de l'object 'SqlLiteDatabase' et l'appel à la méthode "close()".

De plus, ce design pattern permet de ne pas avoir deux ou plusieurs objet 'SqlLiteDatabase' simultanément. Si cela était le cas, nous ne saurions pas réellement à quelle base de données chaque requête ferait référence. Par conséquent, ce choix de design semblait être une évidence.

Pour afficher une table à la console, j'ai pris la décision de créer une classe à part 'Displayer'. Cela permet de bien distinguer clairement la partie logique de l'affichage à la console.

### Vérification des requêtes

Chaque requête est vérifié directement lors de la création de l'objet, dans son constructeur via la méthode "check_request()". Cette vérification ne repose que sur le schéma de la relation, et ne fait pas intervenir la base de données.

Chaque vérification dépend de la requête. Par exemple, la requête 'Union' doit avoir deux relations ayant les mêmes attributs tandis que 'Rename' doit juste vérifier que l'attribut que l'on veut renommer est présent dans le schéma. Si une requête n'est pas validé, un message d'erreur indiquera que cette requête à provoquer une erreur ainsi que la raison de cette erreur.

Par exemple :

```terminal
Invalid expression.
The (sub-)expression
        Rename('nam', 'nom', Rel(lands))
is invalid because the schema of
        Rel(lands)
which is
        {'name': 'TEXT', 'country': 'TEXT', 'money': 'INTEGER'}
has no attribute :
        'nam'
```

### Execution des requêtes

L'execution d'une requête transforme cette dernière en une requête SQL. Ensuite, celle-ci est executée sur la base de données associée à la requête et, dès lors, une nouvelle table est créée en base de données. Cette méthode a été utilisée pour chaque requête. En résumé, une requête SPJRUD qui est executée réalise les actions suivantes : elle utilise la table créée précedemment, crée une nouvelle table en base de données, et supprime par la suite la table de la requête précédente (sauf si cette table est la table originelle).

Cette architecture a été utilisée après avoir rencontré un problème au cours de l'implémentation (voir section "Difficultés rencontrées/Solutions apportées").

## Fonctionnalités supplémentaires

Pour pouvoir tester les différentes requêtes, la classe "Main" contient deux fonctions :

- La fonction 'test' permet de tester différents cas d'utilisation. Le programme demande à l'utilisateur de choisir parmi plusieurs requêtes. Ce test se base sur la base de données de la question 6 dans le syllabus, et contient également la requête corrigée à la question 23.

- La fonction 'manual' permet à l'utilisateur de tester manuellement des requêtes. Il suffit d'écrire la requête à l'endroit défini dans le code. Bien évidemment, n'importe quelles autres méthodes de la librairie peut aussi être utilisée (voir section "Documentation").

## Difficultés rencontrées/Solutions apportées

Au début, j'envisageais d'effectuer recursivement chaque requétes en appelant la méthode "execute" de chaque requête passée en paramètre. Cette méthode ne prenait en compte que le schema de base de données de la relation. Cela fonctionnait parfaitement au premier abord, mais lorsque j'ai voulu implémenter la requête "rename", un problème m'a forcé à changer mon architecture.

En effet, la requéte "rename" en SQL s'effectue sur une table de la base de données. Or, la méthode "execute" recursive s'effectue uniquement sur le schema de base de données sans avoir une table dans la base de données SQLite. J'ai donc considéré une seconde approche. Toute requête crée une table en base de données qui correspond à la requête demandée. Elle s'effectue donc sur la table de la requête effectué précédemment et en crée une nouvelle. Elle supprime ensuite la table de la requête précédente.

## Documentation

### Utilisation de la librairie

Pour pouvoir utiliser ce module, il faut d'abord l'importer :

```Python
from spjrud_converter import *
```

Comme les requêtes doivent être executées sur une base de données SQLite, il faut ensuite créer un objet 'SqlLiteDatabase' qui prend en paramètre le nom de la base de données (le chemin du fichier .db)

```Python
db = SqlLiteDatabase('database.db')
```

Remarque : une seul objet 'SqlLiteDatabase' peut être actif à la fois (voir la section "Choix d'implémentation" pour la justification de ce choix).

### Objet 'SqlLiteDatabase'

```Python
db.reset()
```

Cette méthode permet d'effacer toutes les tables de la base de données.

Celle-ci peut également prendre une liste en paramètres permettant de spécifier les tables de la base de données à conserver.

```Python
db.reset(['countries', 'lands', 'r', 's'])
```

---

```Python
db.execute()
```

Cette méthode permet d'executer une requête SPJRUD passée en paramètres (voir la section suivante pour les différentes requêtes). Elle affiche également le résultat de la requête dans la console.

---

```Python
db.commit()
```

Cette méthode permet de garder les changements en base de données.

```Python
db.rollback()
```

Cette méthode, inversément à la méthode "commit()" ci dessus, permet d'enlever les changements en base de données depuis le dernier commit.

---

```Python
db.close()
```

Cette méthode met fin à la connexion avec la base de données.

---

```Python
db.rename(nom_table, nouveau_nom_table)
```

Cette méthode renomme la table nommé "nom_table".

---

```Python
db.getTables()
```

Cette méthode retourne toutes les tables contenues en base de données.

---

```Python
db.getTable(table_name)
```

Cette méthode retourne toutes les données contenues dans une table de la base de données. Le paramètres 'table_name' représente le nom de la table dans la base de données.

### Requêtes SPJRUD

```Python
Rel(nom, {schema_relation})
```

- nom : nom de la table en base de données
- schema_relation (optionnel) : schéma de la relation. Si ce paramètres n'est pas spécifié, alors le schéma correspond au schéma de la table en base de données.

---

```Python
SelectCst(comparaison, relation)
```

- comparaison : condition de sélection (égalité, inégalité, ...)
- relation : la relation sur laquelle effectué la selection "attribut égal constante"

---

```Python
SelectAttr(comparaison, relation)
```

- comparaison : condition de sélection (égalité, inégalité, ...)
- relation : la relation sur laquelle effectué la selection "attribut égal attribut"

---

```Python
Project(liste_attributs, relation)
```

- liste_attributs : tous les attributs que l'on veut récupérer avec la sélection
- relation : la relation sur laquelle effectué la projection

---

```Python
Rename(attribut, nouveau_nom, relation)
```

- attribut : l'attribut à renommer
- nouveau_nom : le nouveau nom à donner à l'attribut
- relation : la relation sur laquelle effectué le renommage

---

```Python
Join(relation_1, relation_2)
```

- relation_1 : la première relation sur laquelle effectué la jointure
- relation_2 : la seconde relation sur laquelle effectué la jointure

---

```Python
Union(relation_1, relation_2)
```

- relation_1 : la première relation sur laquelle effectué la jointure
- relation_2 : la seconde relation sur laquelle effectué la jointure

---

```Python
Diff(relation_1, relation_2)
```

- relation_1 : la première relation sur laquelle effectué la jointure
- relation_2 : la seconde relation sur laquelle effectué la jointure

## Remarques éventuelles

Coming soon...
