'''
How importing in python works
Importing in Python is the process of loading code from a Python module into the current script.
 This allows you to use the functions and variables defined in the module in your current script, 
 as well as any additional modules that the imported module may depend on.

To import a module in Python, you use the import statement followed by the name of the module.
 For example, to import the math module, which contains a variety of mathematical functions, you would use the following statement:
'''

from math import sqrt, pi 

result = sqrt(90) * pi
print(result) # o/p: 9.486
'''
From keyword: you can also import specififc functions or variables from a module using the from keyword. 
for example, to import only the sqrt function from the math module, 
'''

from math import sqrt

result = sqrt(9)
print(result) # o/p: 3.0


''' we can also import multiple functions or variables at once by separating them with a comma:'''

from math import sqrt, pi
result = sqrt(25)

print(result) 

print(pi)

'''
Importing everything : it's also possible to import all functions and variables from a module using the * wildcard however, this is generally
not recommended as it can lead to confusion and make it harder to understand where specific functions and variables are coming from.
'''

from math import *
result = sqrt(9)

print(result)

print(pi)

'''
Python also allows you to rename imported modules using the as keyword. This can be useful if you 
want to use a shorter or more descriptive name for a module, or
 if you want to avoid naming conflicts with other modules or variables in your code.
'''
'''
The "as" keyword 
'''
import math as m 

result = m.sqrt(25)
print(result) # output: 3.0

print(m.pi) 

'''
The dir function : finally, python has a built-in function called dir that you can use to
 view the names of all the functions and variables defined in amodule. 
 This can be helpful for exploring and understanding the contents of a new module.
'''

import math 

print (dir(math))

'''
This will output a list of all the names defined in the math module, including functions like sqrt and pi, as well as other variables and constants.

In summary, the import statement in Python allows you to access the functions and variables defined in a module 
from within your current script. You can import the entire module, specific functions or variables, or use the * wildcard
 to import everything. You can also use the as keyword to rename a module, and the dir function to view the contents of a module.
'''

