from Rel import *
from Eq import *
from Cst import *
from Select import *

if __name__ == "__main__":
    rel = Rel('Countries', {'country':'TEXT'})
    eq = Eq('country', Cst('Mali'))

    Select(eq, rel)