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

    select = Select(Eq('population', 65658520), rel)
    select1 = Select(Eq('population', 65658520), select)
    result = select1.execute()

    db = SqlLiteDatabase('database.db', '')
    print(db.showTables())
    print(result)

    # project = Project(['name', 'country'], rel)
    # rename = Rename('name', 'nom', project)
    # project1 = Project(['nom'], rename)

    # project1.database.executeRequest(project1.execute())
    #print(rel.database_schema)

    # print(db.showTables())
    # db.dropTable('countries_sel')
    # db.dropTable('countries_sel_sel')
    # print(db.showTables())

    # print(db.showTables())
    # db.createExampleTable()
    # print(db.showTables())
    
