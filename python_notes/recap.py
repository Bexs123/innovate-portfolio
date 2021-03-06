print('Python recap')
print('this is my file for all my python recap notes')

import random # random is a library and it needs to be imported at the top of the code, because code reads and execuates from top to bottom

# use comments to make notes about your code for yourself and for other developers
# Comments can be on multiple lines
# use a hash key at the start of the line for the comment
# you can select the line(s) and use the ctrl and forward slash key to make the line(s) a comment

# variables in this example is greeting, = means it assign the variable to the string and the string is ("hello world")
greeting = "Hello World"

print(greeting) # (greeting) will print out the assigned string in this example it will print out Hello World in the terminal

# Data types, properties and methods
print("this is a string to displaying characters") # this is a string, because the characters are within quotes 
print("536437") # this is still a string because of the quotes
print(12358) # this is an integer because it doesn't have quotes - integer are whole numbers
print(2.3) # floating point
# Boolan (True or False) first letter of true or false needs to be capitial letter
print(True) # Boolan
print(False) # Boolan
print(None) # - Nothing / null data (place holder)

# Strings have methods that we can use to manipulate them, and properties are just information
print(len(greeting)) # len counts the characters and whitespace

print(greeting[1]) # Finds the first character of the string (Index begains at 0) - Answer e

print(greeting[-1]) # Finds the last character of the string because it uses Index -1 - Answer d

# greeting = Object - .upper = method (Dot notation)
print(greeting.upper()) # changes lower case to upper case

# Other Methods (lower(), capitalize(), count(), find(), replace(), and strip()
print("HELLO".lower()) # changes upper case to lower case

print("hello EVERYONE. THIS is innovate".capitalize()) # Changes the first character to capital - also it changes any upper case to lower case

# The count() method returns the number of elements with the specified value
print("The quick brown fox".count("o")) # counts o - Answer is 2
print("The quick brown fox fox fox".count("fox")) # counts fox - Answer is 3
print("The quick brown fox  fox  fox".count("fox  ")) # counts fox - Answer is 2 because of the amount of whitespace inbetween each fox

print("TheT quick brown fox".find("T")) # Answer is Index 0 because it is the first occurrence of the specified value
print("The quick brown fox".find("fox")) # find() in this example will find the word fox and the - Answer is 16 (inculdeds whitespace)

# Example of the find() method returing -1, it returns -1 because the value is not found.
print("The quick brown fox".find("dog"))# Answer is -1

print("The quick brown fox".replace("fox", "frog")) # In this example it will replace all the fox words to frog.

print("    The quick brown fox       ".strip()) # strip will strip leading and trailing whitespace

# Libraries
print(random.random()) # Generates a random number between 0 and 1, inculding 0 only.

print(random.uniform(1, 10)) # Generates a random number between 1 and 10, inclusive

print(random.randint(1, 10)) # Generates a random integer between 1 and 10, inclusive

# random is a library in python and you need to import them if you want to use them.
# To import the library you need to go top of the page and type: - import random

# another way of importing the libraries is:-
# from random import random, randint, uniform
# print(random())
# print(uniform(1, 10))
# print(randint(1, 10))
# Both the same

# Variables

# In everyday life we can store items in boxes to retrieve later.
# You can store all different types of items can be stored in the box at different times.
# In coding you can give variables names so we can access things inside them.

# When naming variables python uses snake_case

my_name = "Boris"
my_age = 21
student = False

print(my_name, my_age, student) # Answer Boris, 21, False

# concatenate
print("Hello my name is", my_name) # Answer Hello my name is Boris
print("I am", my_age) # Answer I am 21

print("Hello my name is " + my_name) # Hello my name is Boris
print("I am" + my_age) # Answer - TypeError: can only concatenate str (not "int") to str
# All the error means is that you can only concatenate or link strings together, not integer to strings

# Concatenation only works on string data types

# Legacy code, all this means that it is outdated, however it can still be read within the websites, but it is best practice to write code in the new format.
# {} are used for placeholders, it just means that you can add data later.

# .format() is the older way of writing strings
print("Hello my name is {} and I am {} years old".format(my_name, my_age))
# Place the variables into the brackets after .format, the variables have to go in the correct order of the placeholders.

# f strings, new best practise, f strings are much cleaner to write and read then using .format.
print(f"Hello my name is {my_name} and I am {my_age} years old")

# Assignment operators (=, *=, +=, /=, -=) are used to assign values to variables
# Example:- +=
# x +=3 is the same as x = x +3

# Example 1
balance = 450
amount = 45

balance = amount + balance
print(balance) # Answer 495

# Example 2
balance = 450
amount = 45

balance += amount
print(balance) # Answer 495

# Example 2 uses the DRY method, it shorter to write and you are not repearting yourself.

# Arithmetic Operators
print(36+8) # Example of an addition - Answer is 44
print(15-5) # Example of a subtraction - Answer is 10
print(5*3) # Example of a multiplication - Answer is 15
print(2**2) # Example of power too or exponentiation Operator - Answer is 4
print(15/3) # Example of division - Answer is 5
print(13%1) # Example of a modulus% - Answer is 0 - Modulus shows the remainder of a division
print(10%3) # Example of a modulus% - Answer is 1

# Order of Operation PEMDAS:
# P - Parenthese
# E - Exponent
# M - Multiplication
# D - Division
# A - Addition
# S - Subtraction

# Input() - allows whatever a user types into the terminal to be saved to a variable - in this case response
input("What is your name?") # Saved in the random memory of the computer

answer = input("What is your name?") # Save as an variable, whatever the user types will be saved to the variable answer.

# \n is an ecaspe character \n will print the answer in a newline
answer = input("What are you going to do today? \n")
print(answer)

# if else
# Example 1
music = "classical"

if music == "classical": # == is a comparison operators
    print("Oh no! It's classical music again.")
elif music == "no music":
    print("Ahh, peace and quiet")
else: # doesn't need comparison operator
    print("Nice and noisy.")
# Answer - Oh no! It's classical music again.
    
# Example 2
music = "no music"

if music == "classical": # == is a comparison operators
    print("Oh no! It's classical music again.")
elif music == "no music":
    print("Ahh, peace and quiet")
else: # doesn't need comparison operator
    print("Nice and noisy.")
# Answer - Ahh, peace and quiet

# Example 3
music = "pop"

if music == "classical": # == is a comparison operators
    print("Oh no! It's classical music again.")
elif music == "no music":
    print("Ahh, peace and quiet")
else: # doesn't need comparison operator
    print("Nice and noisy.")
# Answer - Nice and noisy

# comparison operators checks the if else statements are True or False
# == Equal - this operator checks if the value on the left of the operator is equal to the one on the right
# != Not equal - it checks if the value on the left of the operator is not equal to the one on the right.

# Relational Operator - carries out the comparsion between operands
# Greater than or equal to >= - checks if the value on the left of the operator is greater than or equal to the one on the right.
# Greater than > - checks if the value on the left of the operator is greater than the one on the right.
# Less than or equal to <= - check if the value on the left of the operator is lesser than or equal to the one on the right
# Less than - checks if the value on the left of the operator is lesser than the one on the right

# An example of using Greater than
num = 90
num2 = 290

if num > num2:
    print(f"{num} is bigger")
elif num2 >num:
    print(f"{num2} is bigger")
else:
    print("Both are equal")
    
# logical operator and (both sides must be true)
# These are conjunctions that you can use to combine more than one condition.
# There are three logical operator:- and, or, and not.

# and Operator - if the conditions on both sides of the operator are true, then the expression as a whole is true.

# or Operator - The expression is false only if both the statements around the operator are false. Otherwise, it is true.

# not Operator - This inverts the Boolean value of an expression. It converts True to False, and False to True

# Example of an and operator
place ="MCR"
weather = "cloudy"

if place == "MCR" and weather == "Sunny":
    print("Check again")
elif place == "MCR" and weather == "Rain":
    print("Obvs")
else:
    print("wait, it isn't raning")

# Example of or logical operator 
day = "saturday"

if day == "saturday" or day == "sunday":
    print("It's the weekend!")
else:
    print("When's the weekend?")

# Example 2
day = "sunday"
bank_hol = True

if day == "saturday" or day == "sunday" or bank_hol:
    print("A day off")
else:
    print("off to Innovate we go")

# Functions

# def is the keyword for defining a function.

# Example of Function
def light_switch():
    print("who turned out the lights?")
    
light_switch() # call the function
    
# Example of a Function with parameters - Parameter in this example is amount and accnum
def cash_withdrawal (amount, accnum):
    print(f"Withdrawing {amount} from account {accnum}")
    
cash_withdrawal(300, 50449921) # both values are arguments
cash_withdrawal(20, 53428091)
cash_withdrawal(5000, 12345678)

#Lists
fav_songs = [
    "Bring Me to Life - Evancesences",
    "walk on water - Milk Inc",
    "You stole the sun from my heart - Manic Street Preachers"
]

print(fav_songs) # It will print all the fav_songs list
print(fav_songs[2]) # It will only print out the item in the list at Index position 2
# Answer "you stole the sun from mu heart - Manic Street Preachers" 
print(len(fav_songs)) # Print out the number of items in the list - Answer is 3 because there are three songs in the list.

fav_songs[1] = "Left Outside Alone - Anastacia" # Replaces th list item at Index position 1 to the new list item.
# Index 1 was "walk on Water - Milk Inc" it will become "Left outside Alone - Anastacia"

# .append() method adds to the end of the list
fav_songs.append("Rule the World - Take That")

# .pop() method - it will remove from the end of the list
fav_songs.pop()
print(fav_songs)

# Example of a .remove() method - removes the banana from the list
fruits = ['apple', 'banana', 'cherry']
print(fruits)

fruits.remove("banana")
print(fruits)

# Example of reverse() method - Makes the last item in the list first and the first item last
cars = ['Golf', 'Ferrari', 'BMW', 'Volo']
print(cars)
# Answer - ['Golf', 'Ferrari', 'BMW', 'Volo']

cars.reverse()
print('Reversed List:', cars)
# Answer - Reversed List: ['Volo', 'BMW', 'Ferrari', 'Golf']

# Example of .sort() - sorts the list ascending by default
cars = ['Golf', 'Ferrari', 'BMW', 'Volo']
print(cars)
# Answer - ['Golf', 'Ferrari', 'BMW', 'Volo']

cars.sort()
print(cars)
# Answer - ['BMW', 'Ferrari', 'Golf', 'Volo']

# Eample of .extend method - adds the specified list element (or any iterable) to the end of the current list.
cars = ['Golf', 'Ferrari', 'BMW', 'Volo']
print(cars)
# Answer - ['Golf', 'Ferrari', 'BMW', 'Volo']
fruits = ['apple', 'banana', 'cherry', 'orange']
cars.extend(fruits)
print(cars)
# Answer - ['Golf', 'Ferrari', 'BMW', 'Volo', 'apple', 'banana', 'cherry', 'orange']

# For Loops
# You can call call the fav_songs list by using the index position
print(fav_songs[0])
print(fav_songs[1])
print(fav_songs[2])
# Using this method to call fav_song list is too long and it will get to messy especially when you have for example 100 items in the list.

# lists are iterable
# for is the keyword and it starts the loop
# i is just a variable, it is just refering to the Index

# The loop will sequences three times in this example because they are only three items in this example

# i is just a variable name, i stands for index, which is widly used in for loops.
for i in fav_songs:
    print(i) 
# The action taken is to print each fav_song as looping through the list, one at a time. i is updating everytime it reaches a new value in the sequences.

for i in range(10):
    print(i)
# Answer it will print 0 - 9
    
# 0 is the start num 10 is the stop and 1 is the step
for i in range(0, 10, 1):
    print(i)
        
for i in range(10, -1, -1):
    print(i)
    
# for loops run a finite, or limited number of times.
        
# While Loops

# A while loop will run infinitely and do it's job until a condition is meet.

# Infinite loops - is a sequence of instructions that, as written, will continue endlessly, unless an external intervention.

# To stop the infinity loop in the terminal you will have to press ctrl + c but will have to press ctrl + c at least twice. Or you can use the bin icon in the terminal which will kill the terminal.

##############################################################
#  # Example of inflatatly while loops                       #
#   # - To kill while loop ctrl and c inside the termainal   #
#                                                            #
#   # num = 0                                                #
#                                                            #
#   # while num != 10:                                       #
#   #     print(num)                                         #
#                                                            #
##############################################################  

num = 0 

while num < 10: # Less than comparison operators
    num += 1
    print(num)
# Answer starts at 1 and ends with 10
    
# Random Number Generator
# pseudocode - It us a detailed yet readable description of what a computer program or algorithm must do.

# num 1 - My number
# num 2 - comp number
# compare them
# While they don't match computer guesses again
# When they match, Say "Well Done"

my_num = 16
comp_num = random.randint(1, 50)

while my_num != comp_num:
    print(f"The numbers {my_num} and {comp_num} do not match")
    comp_num = random.randint(1, 50)
    
    print(f"The numbers {my_num} and {comp_num} match")