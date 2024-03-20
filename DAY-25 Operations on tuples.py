'''
Tuples are immutable, hence if you want to add, remove or change 
tuple items, then first you must convert the tuple to a list. 
Then perform operation on that list and convert it back to tuple.
'''

countries = ("Spain", "italy", "india", "England", "germany")
temp = list(countries)
temp.append("Russia")
temp.pop(3)
temp[2] = "Finland"
countries = tuple(temp)
print(countries)

'''
count() Method
The count() method of Tuple returns 
the number of times the given element appears in the tuple.
Syntax:
tuple.count(element)

'''

Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple1.count(3)
print('Count of 7 in Tuple1 is:', res)

'''
index() method
The Index() method returns the first occurrence of the given element from the tuple.

Syntax:
tuple.index(element, start, end)

Note: This method raises a ValueError if the element is not found in the tuple.

'''
Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple.index(3)
print('First occurrence of 3 is', res)