#elif 
'''
num = int(input("Enter the value of num :"))
if (num<0):
    print("number is negative.")
elif(num==0): # elif kei baad jo agle line mei space de raha hu woh indentation error hai
       print("NUmber is zero.")
elif (num==999):
       print("Number is special.")
else:
       print("Number is positive.")


       print("I am happy now")

'''
       # nested else if 

num = 45
if(num<0):
      print("Number is negative.")
elif (num> 0):
 if(num<=10): 
       print("Number is between 1-10")
 elif(num>10 and num <=20):
         print("Number is between 11-20")
else: 
    print("Number is greater than 20")

 
