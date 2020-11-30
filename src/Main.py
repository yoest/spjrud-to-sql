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

    rel = Rel('Countries', {'name':'TEXT', 'country':'TEXT', 'population':'INTEGER'})
    # rel.database.exampleAddValue()

    project = Project(['name', 'country'], rel)
    project.execute()
