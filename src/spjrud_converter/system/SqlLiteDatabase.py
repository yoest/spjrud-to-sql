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
        self.save_state()

        # Design pattern Singleton
        if SqlLiteDatabase.instance == None:
            SqlLiteDatabase.instance = self
        else:
            raise Exception("There is already an opened database")

    @staticmethod 
    def get_instance():
        """ Design pattern Singleton : access with static method """
        if SqlLiteDatabase.instance == None:
            raise Exception("You have to create a SqlLiteDatabase before using request")

        return SqlLiteDatabase.instance

    def save_state(self):
        """ Save the current state of the database """
        # Transform the list of tuple in a simple list of string
        self.initial_state = []
        for table in self.get_tables():
            self.initial_state.append(table[0])
            
    def execute(self, spjrud_request):
        """ Execute the [spjrud_request] and show the result """
        result = spjrud_request.execute()
        
        displayer = Displayer(spjrud_request.database_schema, result)
        displayer.show()

    def commit(self):
        """ Commit the change into the database """
        self.save_state()
        self.connexion.commit()

        print("[Changes commit to the database]")
        print("-- [Current database " + str(self.get_tables()) + "]")

    def rollback(self):
        """ Rollback the change into the database """
        # We cannot use 'rollback()' of sqlite because there is a bug
        # with the library when you start a transaction in multiple methods
        self.reset(self.initial_state)
        self.connexion.commit()

        print("[Changes rollback from the database]")
        print("-- [Current database " + str(self.get_tables()) + "]")

    def close(self):
        """ Close the connexion """
        SqlLiteDatabase.instance = None
        self.connexion.close()

    def reset(self, initial_tables=[]):
        """ reset the database to its initial version """
        # Save the new state
        self.initial_state = initial_tables

        for table in self.get_tables():
            if (not initial_tables) or (not table[0] in initial_tables):
                self.drop_table(table[0])

        self.connexion.commit()

    def rename(self, table_name, new_table_name):
        """ Rename a table from [table_name] to [new_table_name] """
        self.connexion.execute("ALTER TABLE " + table_name + " RENAME TO " + new_table_name + ";")
        
    def get_schema(self, rel_name):
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

    def execute_request(self, table_name, request, old_name=""):
        """ execute the [request] which create a table named [table_name].

            [old] contains the name of the table on which we execute the request
            only if we need to edit this table (example: rename request).
        """

        # Create a new table from the request
        # We don't use only the request because the query 'RENAME' has to be execute
        # on a new table, and so we have to create a table for each request to make
        # the algorithm recursive
        if not old_name:
            self.connexion.execute("CREATE TABLE " + table_name + " AS " + request)
        else:
            self.connexion.execute("CREATE TABLE " + table_name + " AS SELECT * FROM " + old_name + ";")
            self.connexion.execute(request)

    def get_tables(self):
        """ Show names of tables in the database """
        result = self.connexion.execute("SELECT name FROM sqlite_master WHERE type='table';")
        return result.fetchall()

    def get_table(self, table_name):
        """ Show one specific table """
        result = self.connexion.execute("SELECT * FROM " + table_name + ";")
        return result.fetchall()

    def drop_table(self, table_name):
        """ Drop the table named [table_name] """
        self.connexion.execute("DROP table IF EXISTS " + table_name + ";")

    def create_example_table(self):
        """ Create tables for example """
        # Table 'employe'
        self.connexion.execute("CREATE TABLE employe (NrEmp TEXT, Dept TEXT, Pourcent INTEGER);")
        self.connexion.execute("INSERT INTO employe (NrEmp,Dept,Pourcent) VALUES('E1','Info',40);")
        self.connexion.execute("INSERT INTO employe (NrEmp,Dept,Pourcent) VALUES('E1','Bio',60);")
        self.connexion.execute("INSERT INTO employe (NrEmp,Dept,Pourcent) VALUES('E2','Eco',100);")
        self.connexion.execute("INSERT INTO employe (NrEmp,Dept,Pourcent) VALUES('E3','Bio',50);")
        self.connexion.execute("INSERT INTO employe (NrEmp,Dept,Pourcent) VALUES('E3','Eco',50);")
        self.connexion.execute("INSERT INTO employe (NrEmp,Dept,Pourcent) VALUES('E4','Eco',100);")
        self.connexion.execute("INSERT INTO employe (NrEmp,Dept,Pourcent) VALUES('E5','Eco',50);")
        self.connexion.execute("INSERT INTO employe (NrEmp,Dept,Pourcent) VALUES('E5','Bio',25);")
        self.connexion.execute("INSERT INTO employe (NrEmp,Dept,Pourcent) VALUES('E5','Info',25);")

        # Table 'departement'
        self.connexion.execute("CREATE TABLE departement (NomDept TEXT, Budget INTEGER, Chef TEXT);")
        self.connexion.execute("INSERT INTO departement (NomDept,Budget,Chef) VALUES('Info',5000,'E1');")
        self.connexion.execute("INSERT INTO departement (NomDept,Budget,Chef) VALUES('Bio',3500,'E1');")
        self.connexion.execute("INSERT INTO departement (NomDept,Budget,Chef) VALUES('Eco',4000,'E5');")