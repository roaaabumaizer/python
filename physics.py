electric_charge = 4 
electric_voltage = 2

print("You are given the Electric charge which equals = 4C in 1 second and Elctric Voltge which equals= 2V. ")
   
while True:
     
     user = input("Please solve for Resistnce using the information given in the question and type 'done' when finsihed ")
    
     if user == "done":
        resistance = electric_voltage / electric_charge
        user_answer = float(input("Enter your answer for Resistance: "))
     
     if user_answer == resistance:
            print("You are correct")
            break
     else:
         print("You are not correct. Please try again")
     









    
    
    
    return total

result = my_function()
print("The sum is:", result)):  
Equ1= equ()
options = {
    "help": Equ1.Echarge,
    "start and stop": Equ1.time,
    "quit": Equ1.intensity,
    "":Equ1.volatge,
    "":Equ1.resistence
    }
user = input("Enter an option(Help, Start and stop, Quit): ")
for user in options:
 options[user]()
else:
    print("Invalid choice")
