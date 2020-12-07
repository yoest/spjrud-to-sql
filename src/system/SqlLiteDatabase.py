import sqlite3

class SqlLiteDatabase:
    """ This class manage the sql database 

    Attributes:
        path        path of the .db file
        rel_name    name of the relation linked to this database object
    """
    def __init__(self, path, rel_name):
        self.path = path
        self.rel_name = rel_name

        # connexion = sqlite3.connect(self.path)
        # connexion.execute("DROP TABLE " + self.rel_name + ";").fetchall()
        # connexion.commit()
        # connexion.close()

    def getSchema(self):
        """ Get the schema of the relation """
        result = {}
        self.exist()

        connexion = sqlite3.connect(self.path)
        request = connexion.execute("PRAGMA table_info('" + self.rel_name + "')").fetchall()
        
        # The form of the request is, for example :
        # [(0, 'name', 'TEXT', 0, None, 0), (1, 'devise', 'TEXT', 0, None, 0), (2, 'population', 'INTEGER', 0, None, 0)]
        for column in request:
            result[column[1]] = column[2]

        connexion.commit()
        connexion.close()

        return result

    def exist(self):
        """ Check if the table exist """
        connexion = sqlite3.connect(self.path)

        # check if the table already exist
        exist = connexion.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='" + self.rel_name + "'").fetchone()

        # if exist is 1, then the table exists
        if not exist[0] == 1 : 
            raise Exception("Table '" + self.rel_name + "' doesn't exist.")

        connexion.commit()
        connexion.close()

    def checkDatabase(self, database_schema):
        """ Create a table with the database schema : [database_schema] """
        self.exist()

        connexion = sqlite3.connect(self.path)

        # Not the same relation
        if not (database_schema == self.getSchema()):
            raise Exception("Table '" + self.rel_name + "' is not the same than the one in the database.")

        connexion.commit()
        connexion.close()

    def executeRequest(self, table_name, request, old_name=""):
        """ execute the [request] which create a table named [table_name].

            [old] contains the name of the table on which we execute the request
            only if we need to edit this table (example: rename request).
        """
        connexion = sqlite3.connect(self.path)

        # Create a new table from the request
        # We don't use only the request because the query 'RENAME' create obligatorily
        # a new table, and so we have to create a table for each request to make the
        # algorithm recursive
        if not old_name:
            connexion.execute("CREATE TABLE " + table_name + " AS " + request)
        else:
            connexion.execute("CREATE TABLE " + table_name + " AS SELECT * FROM " + old_name + ";")
            connexion.execute(request)

        connexion.commit()
        connexion.close()

    def showTables(self):
        """ Show names of tables in the database """
        connexion = sqlite3.connect(self.path)

        result = connexion.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()

        connexion.commit()
        connexion.close()
        return result

    def showTable(self, table_name):
        """ Show one specific table """
        connexion = sqlite3.connect(self.path)

        result = connexion.execute("SELECT * FROM " + table_name + ";").fetchall()

        connexion.commit()
        connexion.close()
        return result

    def dropTable(self, table_name):
        """ Drop the table named [table_name] """
        connexion = sqlite3.connect(self.path)

        connexion.execute("DROP table IF EXISTS " + table_name + ";")

        connexion.commit()
        connexion.close()

    def createExampleTable(self):
        """ Create two table for example """
        connexion = sqlite3.connect(self.path)

        # Table countries
        connexion.execute("CREATE TABLE countries (name TEXT, country TEXT, population INTEGER);")
        connexion.execute("INSERT INTO countries (name,country,population) VALUES('mons','belgium',50000);")
        connexion.execute("INSERT INTO countries (name,country,population) VALUES('new york','usa',65658520);")
        connexion.execute("INSERT INTO countries (name,country,population) VALUES('madrid','spain',266465);")

        # Table lands
        connexion.execute("CREATE TABLE lands (name TEXT, country TEXT, money INTEGER);")
        connexion.execute("INSERT INTO lands (name,country,money) VALUES('mons','belgium',456192346);")
        connexion.execute("INSERT INTO lands (name,country,money) VALUES('new york','usa',451349294613);")
        connexion.execute("INSERT INTO lands (name,country,money) VALUES('madrid','spain',23164982846);")

        connexion.commit()
        connexion.close()

    def createExampleTableTwo(self):
        """ Create two table for example """
        connexion = sqlite3.connect(self.path)

        # Table countries
        connexion.execute("CREATE TABLE r (a INTEGER, b INTEGER, c INTEGER);")
        connexion.execute("INSERT INTO r (a,b,c) VALUES(1,3,5);")
        connexion.execute("INSERT INTO r (a,b,c) VALUES(1,4,5);")

        # Table lands
        connexion.execute("CREATE TABLE s (a INTEGER, b INTEGER, c INTEGER);")
        connexion.execute("INSERT INTO s (a,b,c) VALUES(1,4,5);")
        connexion.execute("INSERT INTO s (a,b,c) VALUES(2,3,6);")

        connexion.commit()
        connexion.close()