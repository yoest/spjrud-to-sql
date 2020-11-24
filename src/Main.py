from Rel import *
from Eq import *
from Cst import *
from Select import *
from Project import *
from Rename import *
from Join import *
from Union import *
from Diff import *

if __name__ == "__main__":
    rel1 = Rel('Countries', {'name':'TEXT', 'country':'TEXT', 'population':'NUMERIC'})
    rel1bis = Rel('Countries', {'name':'TEXT', 'country':'TEXT', 'population':'NUMERIC'})
    rel2 = Rel('Lands', {'name':'TEXT', 'capital':'TEXT', 'PIB':'NUMERIC'})

    """
    eq = Eq('country', Cst('Mali'))

    select = Select(eq, rel)

    project = Project(['name', 'population'], select)

    rename = Rename('population', 'peoples', project)
    print(rename)

    join = Join(rel1, rel2)
    print(join.request_relation.database_schema)
    """

    diff = Diff(rel1, rel1bis)
    print(diff.request_relation.database_schema)