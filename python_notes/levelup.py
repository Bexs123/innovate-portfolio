#Converting data types 

#int() - interger
#float() - floating points
#str() - string

print(int(5.4))

print(int("54"))
print(int(5.9))

# print(int("nine"))

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


#Scope - global and local variables

light = True

def light_switch():
    global light
    if light:
        print ("whoa! It's bright in here")
        light = False
    else:
        print("who turned out the lights?")
        light = True
        
        light_switch()
        light_switch()
        
#Differences between lists and tuples
#Both are a collection of values
#Lists can handle their values being changed, inserted or deleted
#Tuples are stricter, they act more like constants, less likly to have accidental errors

#List are Mutable - (can be changed)
even_nums = [2, 4, 6, 8, 10]
#Tuples are immutable - (Can't be changed)
odd_nums = (1, 3, 5, 7, 9)


#Slice notation

fav_songs = [
    "Bring Me to Life - Evancesences",
    "walk on water - Milk Inc",
    "You stole the sun from my heart - Manic Street Preachers"
]

#[start:stop:step]
print(fav_songs[1:2:1])

test = "madam"

if test == test[::-1]:
    print(f"Yes! {test} is a palindrome")
else:
    print("It is not a palindrome")


#while True

# while True:
#     print("Run forever")
#Running this code is dangerous because you will have to kill your terminal to get it stop
import random

#this is a while loop that compares a variables and runs under a condition
num = random.randint(1, 50)

while num%2==0:
    print("We like even numbers! Another")
#If the number is odd, the while loop will never ever run
    print("Oh no! An odd number!")
    
    
#Always running
    while True:
        num=random.randint(1, 50)
        print(num)
        if num%2==0:
            print("We like even numbers! Another")
            continue
        else:
            print("An odd number")
            break
#this while loop will always initialise. It might go straight