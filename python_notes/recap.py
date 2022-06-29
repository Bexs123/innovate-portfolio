import random #random is a library and it needs to be imported at the top of the code, because code reads and execuates from top to bottom

# use comments to make notes about your code for yourself and for other developers
# use a hash key at the start of the line for the comment
# you can select the line(s) and use the ctrl and forward slash key to make the line(s) a comment

print('this is my file for all my python notes')

# variables in this example is greeting, = means it assign the variable to the string and the string is ("hello world")
greeting = "Hello World"

print(greeting) #(greeting) will print out the assigned string in this example it will print out Hello World in the terminal

print("this is a string to displaying characters") # this is a string, because it is an characters within quotes 
print("536437") # this is still a string because of the quotes
print(12358) # this is an integer because it doesn't have quotes - integer are whole numbers
print(2.3) # floating point
#Boolan (True or False) first letter of true or false needs to be capitial letter
print(True) # Boolan
print(False) # Boolan
print(None) # - blank / null data (place holder)

#Arithmetic Operators
print(36+8) # Example of an addition - Answer will be 44
print(15-5) #Example of a subtraction - Answer will be 10
print(5*3)#Example of a multiplication - Answer will be 15
print(2**2)#Example of power too or exponentiation Operator - Answer will be 4
print(15/3)#Example of division - Answer will be 5
print(13%1) #Example of a modulus% - Answer will  be 0 - Modulus shows the remainder of a division

#Assignment operators to store values (=, *=, +=, /=, -=)

#Strings have methods that we can use to manipulate them, and properties are just information

print(len(greeting)) # len counts the characters and whitespace

print(greeting[1]) # Finding the first character of the string (Index begains at 0) - Answer e

print(greeting[-1]) # Finding the last character of the string - use Index -1

#greeting = Object - .upper = method (.Dot notation)
print(greeting.upper()) #changes lower case to upper case

#Other Methods (lower(), capitalize(), count(), find(), replace(), and strip()

print("HELLO".lower()) #changes upper case to lower case

print("hello EVERYONE. THIS is innovate".capitalize()) # Changes the first character to capital - also it changes any upper case to lower case

print("This quick brown fox".count("o"))#counts o - Answer is 2

print("This quick brown fox fox fox".count("fox"))#counts fox - Answer is 3
print("This quick brown fox  fox  fox".count("fox  "))#counts fox - Answer is 2 because of the amount of whitespace inbetween each fox

print("This quick brown fox".find("fox"))#find() in this example will find the word fox and the - Answer is 17
#find() method finds the first occurrence of the specified value.

#Example of the find() method returing -1, it returns -1 because the value is not found.
print("This quick brown fox".find("dog"))#Answer is -1

print("The quick brown fox".replace("fox", "frog"))#In this example it will replace all the fox words to frog.

print("    The quick brown fox       ".strip())#strip will strip leading and trailing whitespace

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

# .append

#.pop

#For Loops
#lists are iteratation

for i in fav_songs:
    print(i)

for i in range(10):
    print(i)
    
    #0 is the start num 10 is the stop and 1 is the step
    for i in range(0, 10, 1):
        print(i)
        
    for i in range(10, -1, -1):
        print(i)
        
#While Loops

#Example of inflatatly while loops
# - To kill while loop ctrl and c inside the termainal
# num = 0

# while num != 10:
#     print(num)
    
num = 0 

while num < 10: # Less than companison 
    num += 1
    print(num)
    
# num 1 - My number
# num 2 - comp number

# compare them

# my_num = 
# comp_num = random.randint(1, 50)

# while my_num != comp_num:
    