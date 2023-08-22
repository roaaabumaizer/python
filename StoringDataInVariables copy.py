#Q1
name = "Roaa Abu Maizer"
print(name)

#Q2
import datetime
x = datetime.datetime.now()
print("The curent month is "+ x.strftime("%b"))

#Q3
x = "Roaa"
y = 18 
txt = "My name is {} and I am {} years old"
print(txt.format(x, y))



#Q1*
def my_function():
    print("Roaa Abu Maizer")

my_function() 

#Q2*
import datetime
def my_function():
    x = datetime.datetime.now()
    print("The current month is " + x.strftime("%b"))

my_function()

#Q3*
def my_function(fname, age):
       print("My name is " + fname +  " and I am " + age + " years old")

my_function("Roaa", "18")
