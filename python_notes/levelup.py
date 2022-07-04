print('python level up')

# Converting data types 

# int() - creates an integer data type
# float() - creates a floating point data type
# str() - creates a string data type

# The process of converting data types is known as casting

print(int(5.4)) # Answer 5 - Converting floating point into int
print(int("54")) # Answer 54
print(int(5.9)) # Answer 5

print(type(int("54"))) # Answer <class 'int'>

print(int("hello world")) # Answer ValueError: invalid literal for int() with base 10: 'hello world'

print(float(54)) # Answer 54.0
print(float("54")) # Answer 54.0
print(type(float(54))) # Answer <class 'float'>

print(str(23)) # Answer 23 (Integer)
print(str(21.6)) # Answer 21.6 (Floating point)

# Input takes from the user, it is always a string even if we type number and it can be limited to what we do with it.

# Example without casting
# It will produce an error, because you can not add int and str together without casting.
balance = 300

deposit = input("how much do you want to deposit? \n")

balance += deposit

print(f"you have {balance}") # TypeError: unsupported operand type(s) for +=: 'int' and 'str'

# Example with casting
balance = 2500

deposit = int(input("how much do you want to deposit? \n"))

balance += deposit

print(f"you have {balance}")

# Truthy and Falsy

# Falsy values:-
# Empty string ""
# Integer value 0
# Floating point value 0.0

# Everything else is Truthy

print("What is your name?")
name = input()

if name: # equivalent of if name == True - checking if name has a value
    print(f"Welcome {name} to Innovate")
else: # If the user enters a Falsy value, the else condition is met
    print("you did not submit a name")
    
# Not operator 
# - != operator - which means 'not equal to' - The 'not operator is similar

print(not True) # Answer False
print(not False) # Answer True

day = "Monday"
bank_hol = True

if day == "saturday" or day == "sunday" or bank_hol: # bank_hol looks for a Truthy value
    print("Oh yes a day off")
else:
    print("off to Innovate we go")

# Example of a not operator
allowed = ["Debbie", "Dean", "Joyce", "Mick"]
name = input("What is your name? \n")

while name not in allowed:
    print("Your name isn't on the list")
    print("try again")
    name=input("What is your name")
    
    print("You can come in")
        
bool = False

if bool != True:
    print(False)
else:
    print(True) # Answer is False

# Try/Except statements have very similar syntax to if/else statements
# There to help you catch any errors without your program breaking

deposit = int(input("How much do you want to deposit")) # This will cause an fatal error when the full code will stop, and to prevent fatal error you can use try and except.


def add_up():
    num1 = input("What is the first number you'd like to add up? \n")
    num2 = input("What is the second number you'd like to add up? \n")
    print(num1 + num2)
add_up()
# input is always strings, it is not an arithmetic operator, it will concatenate the strings so example num1 = 5 and num2 150 Answe will be 5150.

# There was no error message becasue it didn't find any errors to catch. The program did what we asked it to do.


def add_up():
    num1 = input("What is the first number you'd like to add up? \n")
    num2 = input("What is the second number you'd like to add up? \n")
    print(int(num1 + int(num2)))
add_up()

# Input num1 and num2 works however print(int(num1 + int(num2))) it will cause a fatal error and this is where you need to use a try and except

# Using the try and except
def add_up():
    num1 = input("What is the first number you'd like to add up? \n")
    num2 = input("What is the second number you'd like to add up? \n")
    
    try: # the program will run if this action can be performed
        print(f"{num1} + {num2} is {(int(num1) + int(num2))}!")
        
    except: # where it can't excute the code, we provide a separate case using except
        print("Please use numbers only")
        print("Try again")
        add_up() # call the function so the user can try again
add_up()

# Scope - global and local variables

light = True # global variable outside of a function, exists everywhere in the code

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
        
# Differences between lists and tuples
# Both are a collection of values

# Lists vs tuples
# Lists are mutable and Changeable
# Tuples are immutable and unchangeable

# Lists have multiple built-in methods to change the calues they hold
# Tuples do not have any methods to change the values they hold.

# Lists can handle their values being changed, inserted or deleted as part of the program.
# Tuples are stricter - they act more like constants, with less room for accidental errors, unlike lists.


# List are Mutable - (can be changed) list use square brackets []
even_nums = [2, 4, 6, 8, 10]
print(even_nums) # Answer [2, 4, 6, 8, 10]
even_nums.append(8)
print(even_nums) # Answer [2, 4, 6, 8, 10, 8] adds the 8 at the end
even_nums.insert(0,0) # Index goes Object goes next
print(even_nums) # Answer [0, 2, 4, 6, 8, 10, 8]
even_nums.insert(1,20)
print(even_nums) # Answer [2, 20, 4, 6, 8, 10, 8]

# Tuples are immutable - (Can't be changed) tuples use parentheses brackets ()
odd_nums = (1, 3, 5, 7, 9)
print(odd_nums) # Answer (1, 3, 5, 7, 9)
odd_nums.append(17) # Will not work on a tuple
print(odd_nums) # Answer AttributeError: 'tuple' object has no attribute 'append'

# Slice notation

# Slicing lists is useful method for working with data

fav_songs = [
    "Bring Me to Life - Evancesences",
    "walk on water - Milk Inc",
    "You stole the sun from my heart - Manic Street Preachers",
    "Crash and Burn - Savage Garden",
    "Behind Blue Eyes - The Who",
    "November Rain - Guns N Roses"
]

# [start:stop:step]
print(fav_songs[1:2:1]) # Answer Walk on water - Milk Inc

print(fav_songs[0:3:1]) # Answer Behind Blue Eyes -The Who

print(fav_songs[1:4:1]) # ['walk on water - Milk Inc', 'You stole the sun from my heart - Manic Street Preachers', 'Crash and Burn - Savage Garden']

print(fav_songs[2:2:2]) # ['walk on water - Milk Inc', 'You stole the sun from my heart - Manic Street Preachers', 'Crash and Burn - Savage Garden']

print(fav_songs[2:4]) # ['walk on water - Milk Inc', 'You stole the sun from my heart - Manic Street Preachers', 'Crash and Burn - Savage Garden']

print(fav_songs[5]) # Answer November Rain - Guns N Roses

# Palindrome Challenge
test = "madam"

if test == test[::-1]:
    print(f"Yes! {test} is a palindrome")
else:
    print("It is not a palindrome")


# while True

# while True:
#     print("Run forever")
# Running this code is dangerous because you will have to kill your terminal to get it stop
import random

# this is a while loop that compares a variables and runs under a condition
num = random.randint(1, 50)

while num%2==0:
    print("We like even numbers! Another")
# If the number is odd, the while loop will never ever run
    print("Oh no! An odd number!")
    
    
# Always running
    while True:
        num=random.randint(1, 50)
        print(num)
        if num%2==0:
            print("We like even numbers! Another")
            continue
        else:
            print("An odd number")
            break
# this while loop will always initialise. It might go straight