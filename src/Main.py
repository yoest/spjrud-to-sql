from relations.Rel import *
from relations.Cst import *
from relations.SelectCst import *
from relations.SelectAttr import *
from relations.Project import *
from relations.Rename import *
from relations.Join import *
from relations.Union import *
from relations.Diff import *

from comparison.Eq import *
from comparison.Gt import *
from comparison.Lt import *

from system.SqlLiteDatabase import *
from system.Displayer import *

if __name__ == "__main__":

    request = {
        #SelectCst(Eq('population', 65658520), Rel('countries')),
        SelectAttr(Eq('name', 'nom'), Join(Rel('countries'), Rename('name', 'nom', Rel('lands')))),
        #Rename('name', 'nom',  Rel('countries')),
        #Project(['name', 'country'], Rel('countries')),
        #Join(Rel('r'), Rel('s')),
        #Union(Rel('r'), Rel('s')),
        #Diff(Rel('r'), Rel('s'))
    }

    db = SqlLiteDatabase('database.db')
    print(db.showTables())
    for request in request:
        result = request.execute()

        print(db.showTables())
        print(request)

        displayer = Displayer(request.database_schema, result)
        displayer.show()

    # db = SqlLiteDatabase('database.db', '')
    # print(db.showTables())
    # db.dropTable('countries_lands_join')
    # print(db.showTables())

    # print(db.showTables())
    # db.createExampleTable()
    # print(db.showTables())
    
