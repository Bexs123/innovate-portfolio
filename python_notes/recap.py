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

#\n is an ecaspe character \n will print the answer in a newline
answer = input("What are you going to do today \n?")
print(answer)

#if else
music = "classical"

if music == "classical": #comparsion Operators
    print("Oh no! It's classical music again.")
elif music == "no music":
    print("Ahh, peace and quiet")
else: #doen't need a comparsion operator 
    print("Nice and noisy.")
    
# comparsion is checking the if statements are True or Falese

num=90
num2=290

if num > num2:
    print(f"{num} is bigger")
elif num2 >num:
    print(f"{num2} is bigger")
else:
    print("Both are equal")
    
#logical operator and (both side must be true)
place ="MCR"
weather = "cloudy"

if place == "MCR" and weather == "Sunny":
    print("Check again")
elif place == "MCR" and weather == "Rain":
    print("Obvs")
else:
    print("wait, it isn't raning")
    
#logical operator or

day = "saturday"

if day == "saturday" or day == "sunday":
    print("It's the weekend!")
else:
    print("When's the weekend?")

#functions
#print and input are functions
#def means definie the function

#Example of Function
def light_switch():
    print("who turned out the lights?")
    
    light_switch() #call the function
    
#Example of a Function with parameters
def cash_withdrawal (amount, accnum):
    print(f"Withdrawing {amount} from account {accnum}")
    
    cash_withdrawal(300, 50449921)
    
#Lists
fav_songs = [
    "Bring Me to Life - Evancesences",
    "walk on water - Milk Inc",
    "You stole the sun from my heart - Manic Street Preachers"
]

print(fav_songs)