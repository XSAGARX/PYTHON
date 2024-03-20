'''
readlines() method
The readline() method reads a single line from the file. 
If we want to read multiple lines, we can use a loop.
'''
f = open('myfile.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)

    '''
    The readline() method reads all the lines of the file and returns them as list
    of strings.
    '''
    '''
    writelines() method
The writelines() method in Python writes a sequence of strings to a file.
 The sequence can be any iterable object, such as a list or a tuple.

Here's an example of how to use the writelines() method:
    '''
    f = open('myfile.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()