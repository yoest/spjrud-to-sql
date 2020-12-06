from relations.Rel import *
from relations.Cst import *
from relations.Select import *
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

def testRelation(relation):
    print(f"[Request]  {relation}")
    print(f"[Schema]  {relation.database_schema}")

if __name__ == "__main__":
    # relations = [
    #     Rel('Countries', {'name':'TEXT', 'country':'TEXT', 'population':'INTEGER'}),
    #     Rel('Countries', {'name':'TEXT', 'country':'TEXT', 'population':'INTEGER'}), 
    #     Rel('Lands', {'name':'TEXT', 'capital':'TEXT', 'PIB':'INTEGER'})
    # ]

    # eq = Eq('name', 'mali')
    # select = Select(eq, relations[0])
    # testRelation(select)
    
    # rename = Rename('name', 'nom', relations[0])
    # testRelation(rename)

    # join = Join(relations[0], relations[1])
    # testRelation(join)

    # union = Union(relations[0], relations[1])
    # testRelation(union)

    # project = Project(['name', 'population'], relations[0])
    # testRelation(project)

    # diff = Diff(relations[0], relations[1])
    # testRelation(diff)

    rel = Rel('countries')
    rel1 = Rel('lands')

    select = Select(Eq('population', 65658520), rel)

    join = Join(rel1, select)

    result = join.execute()

    db = SqlLiteDatabase('database.db', '')
    print(db.showTables())

    displayer = Displayer(join.database_schema, result)
    displayer.show()

    # select = Select(Eq('population', 65658520), rel)

    # rename = Rename('name', 'nom', select)
    # rename1 = Rename('population', 'populace', rename)

    # project = Project(['nom', 'populace'], rename1)

    # project = Project(['name', 'country'], rel)
    # project1 = Project(['nom'], rename)

    # project1.database.executeRequest(project1.execute())
    #print(rel.database_schema)

    # db = SqlLiteDatabase('database.db', '')
    # print(db.showTables())
    # db.dropTable('countries_lands_join')
    # print(db.showTables())

    # print(db.showTables())
    # db.createExampleTable()
    # print(db.showTables())
    
