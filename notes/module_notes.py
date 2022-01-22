## importing modules
import random # import everything from the module
random.randint(0,10)

from random import randint, seed # import specific properties from the module
randint(0,10)

## import modules using aliases
math = 3
import math as m
math # => 3
m # => math module 

## importing created modules
import modules.utils as utils
print(utils.max_diff([5,4,1,6]))

## sys.modules and changing module paths
import sys # module to configure interpreter
from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d) # import modules available one directory above