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

    def getSchema(self, rel_name):
        """ Get the schema of the relation """
        result = {}

        connexion = sqlite3.connect(self.path)
        request = connexion.execute("PRAGMA table_info('" + self.rel_name + "')").fetchall()
        
        # The form of the request is, for example :
        # [(0, 'name', 'TEXT', 0, None, 0), (1, 'devise', 'TEXT', 0, None, 0), (2, 'population', 'INTEGER', 0, None, 0)]
        for column in request:
            result[column[1]] = column[2]

        connexion.commit()
        connexion.close()

        return result

    def createTable(self, database_schema):
        """ Create a table with the database schema : [database_schema] """
        connexion = sqlite3.connect(self.path)

        # check if the table already exist
        exist = connexion.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='" + self.rel_name + "'").fetchone()

        # if exist is 1, then the table exists
        if not exist[0] == 1 : 
            request_schema = "("
            for x, value in enumerate(database_schema):
                request_schema += value + ' ' + database_schema[value]

                if(not (x == len(database_schema) - 1)):
                    request_schema += ", "

            request_schema += ")"

            # Create table
            connexion.execute("CREATE TABLE " + self.rel_name + request_schema + ";")

            connexion.commit()
            connexion.close()

    def executeRequest(self, request):
        """ execute the [request] """
        connexion = sqlite3.connect(self.path)

        result = connexion.execute(request)
        print(result.fetchall())

        connexion.commit()
        connexion.close()


    # -- Example value --
    def exampleAddValue(self):
        connexion = sqlite3.connect(self.path)

        # Insert into table
        connexion.execute("INSERT INTO " + self.rel_name + "(name,country,population) VALUES('mons','belgium',50000)")
        connexion.execute("INSERT INTO " + self.rel_name + "(name,country,population) VALUES('new york','usa',65658520)")
        connexion.execute("INSERT INTO " + self.rel_name + "(name,country,population) VALUES('madrid','spain',266465)")

        connexion.commit()
        connexion.close()