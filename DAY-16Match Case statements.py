# match case is the new addition in 3.10
''' to implement switch- cse like charactertistic very similar to if-else functionality, we use match case in python
. if you are coming from the c, c++, or java like langaues then you must have heard of 
switch case statements. 

a match statement will compare the given variable's value to different shapes, also referred to as the pattern. the main idea is to keep 
on comapring the variable with all the present patterns until it fits into one.

the match case statements have three main entitites 
1. the match keyword
2. one or more case clauses
3. expression for each case



'''


x = int(input("Enter the value of x: "))
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4:
        print("case is 4")

    case _ if x!=90:
        print(x, "is not 90")
    case _ if x!=80:
        print(x, "is not 80")
    case _:
        print(x)

       
