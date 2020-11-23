from Rel import *
from Eq import *
from Cst import *
from Select import *
from Project import *
from Rename import *

if __name__ == "__main__":
    rel = Rel('Countries', {'name':'TEXT', 'country':'TEXT', 'population':'NUMERIC'})

    eq = Eq('country', Cst('Mali'))

    select = Select(eq, rel)

    project = Project(['name', 'population'], select)

    rename = Rename('population', 'peoples', project)
    print(rename)