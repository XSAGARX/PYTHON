''' 
python - else in loop : as you have learned before, the else clause is used along with the if statement.
'''

'''
python allows the else keyword to be used with the for and while loops too. the else block appears after the body of the loop. the statements in the else block will be excecuted after all iterations 
are completed. the program exits the loop only after the else block is executed. 


'''

i = 0 
while i<7:
    print(i)
    i = i + 1
    # if i == 4:
    # break

else: 
    print("Sorry no i")


    for x in range (5):
        print("iteration no {} in for loop". format(x+1))
    else: 
        print("else block in loop")
        print("out of loop")

        