#Q1
letter = input("Enter a letter: ")
num = int(input("Enter a Number: "))
i = 0
while i<num:
    print (letter)
    i = i + 1 

#Q2

# c=0
# c=int(input("how mny time to continue the the process? "))
# z=1
# while z<=c  :
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# total = (num1 + num2)

# z=z+1
# user = input("do you want to stop:'yes' or 'no'")
# if user
#    break
#   print(total)


#Q3
c = 0
x = 0

import random

goalnum = (random.randrange(1, 11))

while x!=goalnum:
  x = int(input("Guess the Number: "))
  c+=1
  if goalnum > x:
    print("too low")
  elif goalnum < x:
    print("too high")
  elif goalnum == x:
     break
print("well done     "+ str(c-1))
    


#Q1*    
def my_function():
    letter = input("Enter a letter: ")
    num = int(input("Enter a Number: "))
    i = 0
    while i < num:
        print(letter)
        i = i + 1

my_function()

#Q3*
import random

def my_function():
    c = 0
    x = 0
    goalnum = random.randrange(1, 11)
    
    while x != goalnum:
        x = int(input("Guess the Number: "))
        c += 1
        
        if goalnum > x:
            print("Too low")
        elif goalnum < x:
            print("Too high")
    
    print("Well done! It took you " + str(c) + " attempt/s")

my_function()


