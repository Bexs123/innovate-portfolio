#Converting data types 

#int() - interger
#float() - floating points
#str() - string

print(int(5.4))

print(int("54"))
print(int(5.9))

print(int("nine"))

balance = 100

deposit = input("how much do you want to deposit?")

balance

#give an error, cannot add int and str together without casting

#casting
int(input("how much do you want to deposit?"))


print("What is your name?")
name = input()

if name: # equivalent of if name == True - checking if name has a value
    print(f"Welcome {name} to Innovate")
else: # If the user enters a Falsy value, the else condition is met
    print("you did not submit a name")
    

#Not operator
# print(not True) Expected to be False
# print(not False) Expected to be True


#Try/Except statements have very similar syntax to if/else statements
#There to help you catch any errors without your program breaking

def add_up():
    num1 = input("What is the first number you'd like to add up? \n")
    num2 = input("What is the second number you'd like to add up? \n")
    print(num1 + num2)
add_up()

