#Q1
fav_animal = input("What's your favourite animal? ")
print(fav_animal)

#Q2
fname = input("what's your first name? ")
lname = input("what's your last name? ")
print("Hello" + " " + fname + " " + lname)

#Q3
country = input("enter country: ")
population = input("enter popuation: ")
print(country + " has a population of " + population + " people")



#Q1*
def my_function( ):
    fav_animal = input("What's your favourite animal? ")
    print(fav_animal)

my_function( )

#Q2*
def my_function( ):
    fname = input("what's your first name? ")
    lname = input("what's your last name? ")
    print("Hello" + " " + fname + " " + lname)

my_function( )

#Q3*
def my_function( ):
    country = input("enter country: ")
    population = int(input("enter popuation: "))
    print(country + " has a population of " + str(population) + " people")

my_function( )