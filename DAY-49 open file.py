'''
In python we can amnipulate files through several methods. today we will discuss how to handle files in python. 

Opening a file: before we can perform any operations on a file. we must first open it. py provide the open
() to open a file. it takes two arguments: the name of the file and the mode in which the file should be opened.
the mode can be 'r' for reading 'w' for writing or 'a' for appending.
'''

f = open('myfile.txt', 'r')

'''
By default, the open() functions returns a file object that can be used to read from or write to the file, depending on the mode.

'''

'''
modes in file: There are various modes in which we can open files.

read (r): This mode opens the file for reading only and gives an error if the file does not exist.
 This is the default mode if no mode is passed as a parameter.

write (w): This mode opens the file for writing only and creates a new file if the file does not exist.

append (a): This mode opens the file for appending only and creates a new file if the file does not exist.

create (x): This mode creates a file and gives an error if the file already exists.

text (t): Apart from these modes we also need to specify how the file must be handled. 
t mode is used to handle text files. t refers to the text mode. There is no difference between r and rt or w and wt since text mode is the default.
 The default mode is 'r' (open for reading text, synonym of 'rt' ).

binary (b): used to handle binary files (images, pdfs, etc).
'''
'''
Reading from a file : once we have a file object, we can use various methods to 
read from the file.

the read() method reads the entire contents of the file and returns it as string. 
'''
f = open('myfile.txt', 'r')
contents = f.read()
print(contents)

'''we can then use the write() method to write to the file.'''

f = open ('myfile.txt', 'w')
f.write('Hello, world!')

'''keep in mind that writing to a file will overwrite its contents. if you want to
append toa file insted of overwriting it, you can open it in append mode.'''

f = open('myfile.txt', 'a')
f.write('Hello, world!')

'''
closing a file: It is important to close a file after you are done with it. 
This releases the resources used by the file and allows other programs to access it.

To close a file, you can use the close() method.

'''
f = open('myfile.txt', 'r')
# ... do something with the file
f.close()

'''
The 'with' statement
Alternatively, you can use the with statement to automatically close the file after you are done with it.
'''

with open('myfile.txt', 'r') as f:
    # ... do something with the file