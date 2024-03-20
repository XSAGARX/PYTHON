'''
Finally Clause
The finally code block is also a part of exception handling. When we handle exception using the try and except block,
 we can include a finally block at the end. The finally block is always executed, so it is generally used for doing the concluding tasks
   like closing file resources or closing database connection or may be ending the program execution with a delightful message.
'''

try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
else:
    print("Integer Accepted.")
finally:
    print("This block is always executed.")