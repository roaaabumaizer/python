#Q1
num = int(input())
if num > 100:
    print("larger than 100")
else:
    print("less than 100 is shown")

#Q2
    num = int(input("Enter Test Score: "))
if num > 20:
        print("You Achieved an A")
if 10 < num < 19:
        print("You achived a B")
if num < 10:
        print("You failed")

#Q3
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = input("Would you like (+, -, /, *) the numbers? ")
if sum == "+":
 print(num1+num2)
elif sum == "-":
  print(num1-num2)
elif sum == "/":
  print(num1/num2)
elif sum == "*":
  print(num1+num2)



  #Q1*
def my_function( ):
    num = int(input("Enter Number: "))
    if num > 100:
     print("larger than 100")
    else:
     print("less than 100 is shown")

my_function( )

#Q2*
def my_function( ):
    num = int(input("Enter Test Score: "))
    if num > 20:
        print("You Achieved an A")
    if 10 < num < 19:
        print("You achived a B")
    if num < 10:
        print("You failed")
my_function( )

#Q3*
def my_function():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operation = input("Would you like (+, -, /, *) the numbers? ")

    if operation == "+":
     print(num1 + num2)
    elif operation == "-":
     print(num1 - num2)
    elif operation == "/":
     print(num1 / num2)
    elif operation == "*":
     print(num1 * num2)
    

my_function()
#wont work