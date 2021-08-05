# SPJRUD to SQL converter

This project consists in creating a python application to compile SPJRUD queries to SQL queries. Moreover, this application must check that the SPJRUD query is initially correct.

## Description

### Packages

The classes are separated in 3 different packages:

- The **comparison** package contains all the classes needed for comparisons (for example for the "select" query), i.e. the classes representing "=", ">", ...
- The **relations** package contains all the classes representing queries/relationships (example: "Select", "Join", ...)
- The **system** package contains all the classes necessary for the good functioning of the system (other than "Main") such as the link with the database or the display of a query in the console.

#### Package *comparison*

To represent comparisons, I decided to create a global class that represents an equality. Then, all other comparisons, such as "bigger" or "smaller", inherit from this global class.

#### Package *relations*

It was decided to represent each query with a class named after the query. Each of these inherits from a *Rel* class which represents a relationship. Indeed, each query, once executed, also corresponds to a relation.

Moreover, each query takes as parameters one or more relations which can be :

- a *Rel* object if the relation is a table in a database (or possibly a schema provided by the user).
- One of the classes representing a query if the latter is itself performed on another relation.

Any set of queries therefore contains at least one *Rel* object.

#### Package *system*

I implemented the *SqlLiteDatabase* class using the Singleton design pattern.

To display a table at the console, I decided to create a separate class *Displayer*. This allows to clearly distinguish the logical part from the console display.

### Verification of queries

Each request is checked directly when the object is created, in its constructor via the "check_request()" method. This check is only based on the schema of the relation, and does not involve the database.

Each check depends on the query. For example, the query *Union* must have two relations with the same attributes while *Rename* must just check that the attribute you want to rename is present in the schema. If a query is not validated, an error message will indicate that this query has caused an error as well as the reason for this error.

For example :

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

### Executing queries

The execution of a query transforms it into an SQL query. Then, the query is executed on the database associated with the query and, as a result, a new table is created in the database. This method was used for each query. In summary, a SPJRUD query that is executed performs the following actions: it uses the previously created table, creates a new table in the database, and subsequently deletes the table from the previous query (unless that table is the original table).

## Additional features

In order to test the different requests, the *Main* class contains two functions:

- The "test()" function allows to test different use cases. The program asks the user to choose among several queries.

- The "manual()" function allows the user to test queries manually. It is enough to write the query in the place defined in the code.

## Getting Started

### Dependencies

- sqllite3

### Executing program

Just run the file "main.py" in the source folder.

## Authors

[@Yorick Estievenart](https://github.com/yoest)

## Version History

* 0.1
  * Initial Release

## License

This project is licensed under the GNU General Public License v3.0 License - see the LICENSE.md file for details.