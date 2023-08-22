#Q1
x = 5
y = 7
print(x+y)

#Q2
num = input("what is your first number? ")
numerouno = input("What is your second number? ")
print(numerouno + " divided " + num + " equals 10")
#Q2*
num = int(input("what is your first number? "))
numerouno = int(input("What is your second number? "))
total = (num + numerouno)
print(str(numerouno) + " divided " + str(num) + " equals " + str(total))

#Q3 
num1 = int(input())
num2 = int(input())
num3 = int(input())
x = 2
result = num1+num2 -num3**x
print(result)



#Q1*
def num(x, y):
    print("= " + str(x + y) )
num(5, 7)

#Q2**
def my_function( ):
    num = int(input("what is your first number? "))
    numerouno = int(input("What is your second number? "))
    total = (num + numerouno)
    print(str(numerouno) + " divided " + str(num) + " equals " + str(total))

my_function()
    
#Q3*
def my_function( ):
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    num3 = int(input("Enter Third Number: "))
    x = 2
    result = num1+num2 -num3**x
    print(result)
    
my_function()
