# Object Oriented Programming

# Procedural programming means that the code is read from top to bottom, using this method is good for solo programmers, however when the program becomes more complex then it will be more difficuit to keep track of whats happening.

# When working as part of a software team this is where object oriented programming comes in.

# Object Oriented Programming or OOP for short means we are trying to model objects with our code.

# To create objects you do that by using classes.

# Objects are a group of data and functions. The data stored in objects are referred to as attributes. The functions we call on are called methods.

# Attributes is what it has and methods is what it does.

# OOP It is well known concept / theory om programming, it's all about writing clean code, by doing so it makes the programs easier to maintain. It refers to how you structure your code in order to make it reusable.

# A frequently used analogy to describe OOP is the cookie cutter. Classes are templates for our objects just like cookie cutters are for cookies.
# cookie cutter is the blueprint and the cookies are the object

# Example of procedural programming - the code is read top down

variable_one = 10

# print(variable_one)
# Answer - 10

variable_one += 20
# Answer will be 10 because the print statement has been wrote in between the assignment and the operation.

print(variable_one)
# Answer is 30

variable_one /= 3
print(variable_one)
# Answer 10.0

# scalability - start small and then make it bigger and better, and also removes remove unwanted functions and features.

# Cookie cutter
# class Guitar():
#     def __init__(self, colour, string_no):
#         self.colour = colour
#         self.string_no = string_no

# cookie
# wills_guitar = Guitar ("blue", 6)

# print(wills_guitar)
# <__main__.Guitar object at 0x000001FE42197D60>
# This how to make a custom object


# Example of class Guitar with custom methods
class Guitar:
    def __init__(self, colour, string_no):
        self.colour = colour
        self.string_no = string_no

# classes can be given custom methods change the state of the class or do something
    def play(self):
        print("Noise!")

wills_guitar = Guitar("blue", 6)

wills_guitar.play()
# Noise!

# this empty codespace is an object as well. This is call the main object __main__ it is an hidden object.


# Made from a class called float
example_variable_1 = 3.14152

print(type(example_variable_1))
# <class 'float'>

example_variable_2 = "Hello World"

print(type(example_variable_2))
# <class 'str'>
