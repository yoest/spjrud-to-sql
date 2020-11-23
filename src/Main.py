from Rel import *
from Eq import *
from Cst import *
from Select import *
from Project import *
from Rename import *

if __name__ == "__main__":
    rel = Rel('Countries', {'name':'TEXT', 'country':'TEXT', 'population':'NUMERIC'})
    print(rel.database_schema)

    """
    eq = Eq('country', Cst('Mali'))

    Select(eq, rel)
    """

    project = Project(['name', 'population'], rel)
    print(project.request_relation.database_schema)

    project2 = Project(['population'], project)
    print(project2.request_relation.database_schema)

    rename = Rename('population', 'peoples', project2)
    print(rename.request_relation.database_schema)