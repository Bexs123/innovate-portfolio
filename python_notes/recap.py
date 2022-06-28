import random

# use comments to make notes about your code for yourself and so other developers can 
# use a hash key at the start of the line for the comment
# you can select the line and use the ctrl and forward slash key to make the line a comment

print('this is my file for all my python notes')

# variables in this example is greeting, = means it assign the variable to the string and the string is ("hello world")
greeting = "Hello World"

print(greeting) #(greeting) will print out the assigned string in this example it will print out Hello World in the terminal

print("this is a string to displaying characters") # this is a string
print("536437") # this is still a string because of the quotes
print(12358) # this is an integer because it doesn't have quotes
print(36+8) # this is an example of an calculation 
print(2.3) # floating point
#Boolan (True or False) first letter of true or false needs to be capitial letter
print(True) # Boolan
print(False) # Boolan
print(None) # - blank / null data (place holder)

print(len(greeting)) # len counts the characters

print(greeting[1]) #output is e. Index starts at 0

print(greeting[-1]) #output the last character

#greeting = Object - .upper = method
print(greeting.upper()) #changes lower case to upper case

print("HELLO".lower())

print("hello EVERYONE. THIS is innovate".capitalize()) #changes the first letter to capital

print("This quick brown fox".count("o"))

print("This quick brown fox  fox fox".count("fox"))

print("This quick brown fox".find("fox"))

print("The quick brown fox".replace("fox", "frog"))

print("    The quick brown fox       ".strip())

print(random.random()) #Generates a random number between 0 and 1, inculding 0 only.

print(random.uniform(1, 10)) #Generates a random number between 1 and 10, inclusive

print(random.randint(1, 10)) #Generates a random integer between 1 and 10, inclusive

#random is a library in python and you need to import them if you want to use them.

# can use use from random import random, randint, uniform

my_name = ""
my_age = ""
student = False

print(my_name, my_age, student)

print("Hello my name is ")
#concatenate (concatenating)

#.format()  method allows to use placeholder {}
# {} are for placeholders 
print("Hello my name is {} and I am {} years old".format(my_name, my_age))

#f strings, new best practise
print(f"Hello my name is {my_name} and I am {my_age} years old")

print(49+2)
print(172-72)
print(78*3)
print(8**8)
print(18/3)
print(81%4)

balance=100
amount=20

balance=amount+balance
balance +=amount