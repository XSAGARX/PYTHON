''' Lists : lists are ordered collection of data items .
2. they store multiple items in a single variable.
3. list items are separated by commas and enclosed within square brackets().
4. lists are changeable meaning we can alter them after creation.

5. tuples cannot be changed 
you can put string and boolean inside a list  but you should not because it completely depends on the variable 


  '''

marks = [3,5,6, "Harry", True]
'''

marks = [3,5,6]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])

'''
# negative indexing : similar to positive indexing negative indexing is also used to access items, but from the end of the 
# list. the last item has index[-1], second last item has index[-2], third last item has index[-3] and so on 
'''
print(marks[-3]) # negative index
print(marks[len(marks)-3]) # positive index

print(marks[5-3])# positive index
print(marks[2])# positive index

'''

if "Harry" in marks:
    print("yes")
else:
       print("No")
    

