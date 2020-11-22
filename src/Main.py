from Rel import *
from Eq import *
from Cst import *
from Select import *
from Project import *

if __name__ == "__main__":
    rel = Rel('Countries', {'name':'TEXT', 'country':'TEXT', 'population':'NUMERIC'})
    print(rel.perform())

    """
    eq = Eq('country', Cst('Mali'))

    Select(eq, rel)
    """

    project = Project(['name', 'population'], rel).perform()
    print(project.database_schema)

    project2 = Project(['population'], project).perform()
    print(project2.database_schema)