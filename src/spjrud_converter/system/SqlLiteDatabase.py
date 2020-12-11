import sqlite3

from spjrud_converter.system.Displayer import *

class SqlLiteDatabase:
    """ This class manage the sql database 

    Attributes:
        path            path of the .db file
        keep_changes    keep the changes in the database ?
    """
    instance = None

    def __init__(self, path):
        self.path = path

        # Open a connexion to the database and save the current state
        self.connexion = sqlite3.connect(self.path)
        self.saveState()

        # Design pattern Singleton
        if SqlLiteDatabase.instance == None:
            SqlLiteDatabase.instance = self
        else:
            raise Exception("There is already an opened database")

    @staticmethod 
    def getInstance():
        """ Design pattern Singleton : access with static method """
        if SqlLiteDatabase.instance == None:
            raise Exception("You have to create a SqlLiteDatabase before using request")

        return SqlLiteDatabase.instance

    def saveState(self):
        """ Save the current state of the database """
        # Transform the list of tuple in a simple list of string
        self.initial_state = []
        for table in self.getTables():
            self.initial_state.append(table[0])
            
    def execute(self, spjrud_request):
        """ Execute the [spjrud_request] and show the result """
        result = spjrud_request.execute()
        
        displayer = Displayer(spjrud_request.database_schema, result)
        displayer.show()

    def commit(self):
        """ Commit the change into the database """
        self.connexion.commit()

        print("[Changes commit to the database]")
        print("-- [Current database " + str(self.getTables()) + "]")

    def rollback(self):
        """ Rollback the change into the database """
        # We cannot use 'rollback()' of sqlite because there is a bug
        # with the library when you start a transaction in multiple methods
        self.reset(self.initial_state)
        self.connexion.commit()

        print("[Changes rollback from the database]")
        print("-- [Current database " + str(self.getTables()) + "]")

    def close(self):
        """ Close the connexion """
        SqlLiteDatabase.instance = None
        self.connexion.close()

    def reset(self, initial_tables=[]):
        """ reset the database to its initial version """
        # Save the new state
        self.initial_state = initial_tables

        for table in self.getTables():
            if (not initial_tables) or (not table[0] in initial_tables):
                self.dropTable(table[0])

        self.connexion.commit()
        
    def getSchema(self, rel_name):
        """ Get the schema of the relation """
        result = {}
        self.exist(rel_name)

        request = self.connexion.execute("PRAGMA table_info('" + rel_name + "')").fetchall()
        
        # The form of the request is, for example :
        # [(0, 'name', 'TEXT', 0, None, 0), (1, 'devise', 'TEXT', 0, None, 0), (2, 'population', 'INTEGER', 0, None, 0)]
        for column in request:
            result[column[1]] = column[2]

        return result

    def exist(self, rel_name):
        """ Check if the table exist """
        exist = self.connexion.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='" + rel_name + "'").fetchone()

        # if exist is 1, then the table exists
        if not exist[0] == 1 : 
            raise Exception("Table '" + rel_name + "' doesn't exist.")

    def executeRequest(self, table_name, request, old_name=""):
        """ execute the [request] which create a table named [table_name].

            [old] contains the name of the table on which we execute the request
            only if we need to edit this table (example: rename request).
        """

        # Create a new table from the request
        # We don't use only the request because the query 'RENAME' create obligatorily
        # a new table, and so we have to create a table for each request to make the
        # algorithm recursive
        if not old_name:
            self.connexion.execute("CREATE TABLE " + table_name + " AS " + request)
        else:
            self.connexion.execute("CREATE TABLE " + table_name + " AS SELECT * FROM " + old_name + ";")
            self.connexion.execute(request)

    def getTables(self):
        """ Show names of tables in the database """
        result = self.connexion.execute("SELECT name FROM sqlite_master WHERE type='table';")
        return result.fetchall()

    def getTable(self, table_name):
        """ Show one specific table """
        result = self.connexion.execute("SELECT * FROM " + table_name + ";")
        return result.fetchall()

    def dropTable(self, table_name):
        """ Drop the table named [table_name] """
        self.connexion.execute("DROP table IF EXISTS " + table_name + ";")

    def createExampleTable(self):
        """ Create tables for example """
        # Table 'countries'
        self.connexion.execute("CREATE TABLE countries (name TEXT, country TEXT, population INTEGER);")
        self.connexion.execute("INSERT INTO countries (name,country,population) VALUES('mons','belgium',50000);")
        self.connexion.execute("INSERT INTO countries (name,country,population) VALUES('new york','usa',65658520);")
        self.connexion.execute("INSERT INTO countries (name,country,population) VALUES('madrid','spain',266465);")

        # Table 'lands'
        self.connexion.execute("CREATE TABLE lands (name TEXT, country TEXT, money INTEGER);")
        self.connexion.execute("INSERT INTO lands (name,country,money) VALUES('mons','belgium',456192346);")
        self.connexion.execute("INSERT INTO lands (name,country,money) VALUES('new york','usa',451349294613);")
        self.connexion.execute("INSERT INTO lands (name,country,money) VALUES('madrid','spain',23164982846);")

        # Table 'r'
        self.connexion.execute("CREATE TABLE r (a INTEGER, b INTEGER, c INTEGER);")
        self.connexion.execute("INSERT INTO r (a,b,c) VALUES(1,3,5);")
        self.connexion.execute("INSERT INTO r (a,b,c) VALUES(1,4,5);")

        # Table 's'
        self.connexion.execute("CREATE TABLE s (a INTEGER, b INTEGER, c INTEGER);")
        self.connexion.execute("INSERT INTO s (a,b,c) VALUES(1,4,5);")
        self.connexion.execute("INSERT INTO s (a,b,c) VALUES(2,3,6);")