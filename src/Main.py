from Rel import *
from Eq import *
from Cst import *
from Select import *
from Project import *
from Rename import *
from Join import *
from Union import *
from Diff import *

from SqlLiteDatabase import *

def testRelation(relation):
    print(f"[Request]  {relation}")
    print(f"[Schema]  {relation.database_schema}")

if __name__ == "__main__":
    relations = [
        Rel('Countries', {'name':'TEXT', 'country':'TEXT', 'population':'NUMERIC'}),
        Rel('Countries', {'name':'TEXT', 'country':'TEXT', 'population':'NUMERIC'}), 
        Rel('Lands', {'name':'TEXT', 'capital':'TEXT', 'PIB':'NUMERIC'})
    ]

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

    database = SqlLiteDatabase()
