''' 
Dictionary Methods : dictionary uses several built-in methods for manipulation. they are listed below 


'''

''' update () The update() method updates the value of the key provided to it if teh item already exists in the dictionary, else 
it cretaes a new key-value pair.'''

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)


''' Removinf items from dictionary : 
There are a few methods that we can use to remove items from dictionary.'''

'''
clear(): the clear() method removes all the items from the list.'''

info = {'name': 'sagar', 'age': 22, 'eligible' : True}
info.clear()
print(info)

'''pop(): The pop() method removes the key-value pair whose key is passed as a parameter '''


info = {'name' : 'sagar' , 'age': 22, 'eligible': True}
info.pop('eligible')
print(info)


''' popitem(): the popitem() method removes the last key - value pair from the dictionary.'''

info = {'name': 'sagar', 'age':22, 'eligible': True,
        'DOB': 2002 }
info.popitem()
print(info)


'''del: we can also use the del keyword to remove a dictionary item. '''
info = {'name': 'sagar', 'age': 22, 'eligible': True,
        'DOB': 2200}
del info['age']
print(info)

''' if key is not provided, then the del keyword will delete the dictionary entirely.'''

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info
print(info)