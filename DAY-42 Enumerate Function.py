'''
Enumerate function in python
The enumerate function is a built-in function in Python that allows you to loop over a sequence 
(such as a list, tuple, or string) and get the index and value of each element in the sequence at the same time. Here's a basic example of how it works:
'''


# loop over a list and print the index value of each element 

fruits = ['apple', 'banana', 'mango', 'kela', 'lemon']
for index, fruit in enumerate(fruits):
    print(index, fruit)

    '''
    Changing the start index
By default, the enumerate function starts the index at 0, but you can specify a different starting 
index by passing it as an argument to the enumerate function:
    '''
    # Loop over a list and print the index (starting at 1) and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

    '''
    The enumerate function is often used when you need to loop over a sequence and perform some
      action with both the index and value of each element. For example, you might use it to loop over a
      list of strings and print the index and value of each string in a formatted way:
    '''
    fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(f'{index+1}: {fruit}')

    '''
    In addition to lists, you can use the enumerate function with any other sequence type in Python, 
    such as tuples and strings. Here's an example with a tuple:
    '''

    # Loop over a tuple and print the index and value of each element
colors = ('red', 'green', 'blue')
for index, color in enumerate(colors):
    print(index, color)


    # Loop over a string and print the index and value of each character
s = 'hello'
for index, c in enumerate(s):
    print(index, c)