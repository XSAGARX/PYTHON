'''
joining Sets: Sets in python more or less work in the same way as
 sets in mathematics. We can perform operations
 like union and intersection on the sets just like in mathematics. 

 I. union() and update():
The union() and update() methods prints all items that are present in the two sets. 
The union() method returns a new set whereas update() method 
adds item into the existing set from another set.

'''

cities = {"patna", "mumbai", "delhi", "chandigarh"}
cities2 = {"berlin", "london", "banglore"}
cities3 = {"chennai", "guwahati"}
cities4 = cities.union(cities2).union(cities3)
print(cities4) # output jo hai woh sequence mei hai jab bhi run karoge alag o/p aayega

cities = {"Tokyo", "madrid", "berlin", "delhi"}
cities2 = {"seoul", "africa", "atlantic"} # yaha bhi o/p mei sequence nahi hoga
cities.update(cities2)
print(cities)

'''Intersection and intersection_update(): The intersection() and 
intersection_update()
 methods prints only items that are similar to both the sets. 
The intersection() method returns a new set whereas intersection_update() 
method updates into the existing set from another set. '''

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3) # yaha pe o/p ek sequence mei hota hai jo o/p hota hai wahi same o/p hamesha hota hai 

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.intersection_update(cities2)
print(cities)

'''
III. symmetric_difference and symmetric_difference_update():
The symmetric_difference() and symmetric_difference_update() methods prints only
 items that are not similar to both the sets.
 The symmetric_difference() method returns a new set whereas symmetric_difference_update()
   method updates into the existing set from another set.
'''

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.symmetric_difference_update(cities2)
print(cities)


'''
Set Methods
There are several in-built methods used for the manipulation of set.
They are explained below

isdisjoint():
The isdisjoint() method checks if items of given set are present in another set. 
This method returns False if items are present, else it returns True.
'''

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))

'''
issuperset():
The issuperset() method checks if all the items of a particular 
set are present in the original set. 
It returns True if all the items are present, else it returns False.
'''
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Seoul", "Madrid","Kabul"}
print(cities.issuperset(cities3))

'''
issubset():
The issubset() method checks if all the items of 
the original set are present in the particular set.
 It returns True if all the items are present, else it returns False.
'''
hero ={"salman", "shahrukh", "hrithik", "akshay"}
hero2 = {"salman", "shahrukh"}
hero3 ={"hrithik", "akshay"}
print(hero2, hero3.issubset(hero))

'''
add()
If you want to add a single item to the set use the add() method.
'''

Entrepreneur = {"elon musk", "stevejobs", "ratan tata", "bil gates"}
Entrepreneur.add("gautam adani")
print(Entrepreneur)

'''
update()
If you want to add more than one item, simply create another 
set or any other iterable object(list, tuple, dictionary),
 and use the update() method to add it into the existing set.
'''
companies = {"apple", "microsoft", "spacex", "tesla"}
companies2 = {"boat", "zerodha", "reliance"}
companies3 = {"dabbaur"}
companies.update(companies2,companies3)
print(companies)

'''
remove()/discard()
We can use remove() and discard() methods to remove items form list.
'''
vegetables ={"brinjal", "potato", "tomato"}
vegetables.remove("brinjal")
print(vegetables)

'''
The main difference between remove and discard is that, if we try to delete an item which is not present in set,
 then remove() raises an error,
 whereas discard() does not raise any error.
'''
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Seoul")
print(cities)

'''
pop()
This method removes the last item of the set but the catch is that we don’t 
know which item gets popped as sets are unordered.
 However, you can access the popped item if you assign the pop() method to a variable.
'''

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)

'''
del
del is not a method, rather it is a keyword which deletes the set entirely.
'''
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
print(cities)

'''
NameError: name 'cities' is not defined We get an error because our entire
 set has been deleted and there is no variable called cities which contains a set.

What if we don’t want to delete the entire set,
 we just want to delete all items within that set?
'''
'''
clear():
This method clears all items in the set and prints an empty set.
'''
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)
