''' f string uses for formatting in python using the format method. '''

'''f - string in python : It is a new string formatting mechanism introduced by the PEP 498.
 It is also known as Literal String Interpolation or more commonly as F-strings (f character preceding the string literal).
   The primary focus of this mechanism is to make the interpolation easier.

When we prefix the string with the letter 'f', the string becomes the f-string itself. 
The f-string can be formatted in much same as the str.format() method. 
The f-string offers a convenient way to embed Python expression inside string literals for formatting. '''

val = 'Geeks'
print(f"{val}for{val} is a portal for {val}.")
name = 'Tushar'
age = 23
print(f"Hello, My name is {name} and I' m {age} years old. ")

 # *******************************************************************
char = 'MUNDA'
print(f"{char}for{char} is a people for {char}.")
name = 'SAGAR'
age=21
print(f"Hello, my name is {name} and I ' m {age} years old.")