import sqlite3

class SqlLiteDatabase:
    def __init__(self):
        connexion = sqlite3.connect('test.db')

        # Create table
        connexion.execute("CREATE TABLE Countries (name VARCHAR(20), devise VARCHAR(20), population INTEGER(2));")

        connexion.execute("INSERT INTO Countries (NAME,DEVISE,POPULATION) VALUES ('Mali', 'euro', 11);")

        # Show row
        cursor = connexion.execute("SELECT name, devise, population from Countries")
        for row in cursor:
            print("NAME = ", row[0])
            print("DEVISE = ", row[1])
            print("POPULATION = ", row[2])

        connexion.commit()
        connexion.close()