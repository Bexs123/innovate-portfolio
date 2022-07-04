Object oriented programming (OOP) in Python

Inheritance

It allows us to define a class that inherits all the methods and properties from another class

The parent class is the class being inherited from, and also known as the base class.

Child class is the class that inherits from another class.

To create a child class, send the parent class as a parameter when creating the child class.


Encapsulation
It is one of the fundamental concepts in OOP. It basically wraps data and the methods that work  on data within one unit. It also puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data.



ntroduction to encapsulation in Python
Encapsulation is one of the four fundamental concepts in object-oriented programming including abstraction, encapsulation, inheritance, and polymorphism.

Encapsulation is the packing of data and functions that work on that data within a single object. By doing so, you can hide the internal state of the object from the outside. This is known as information hiding.

A class is an example of encapsulation. A class bundles data and methods into a single unit. And a class provides the access to its attributes via methods.

The idea of information hiding is that if you have an attribute that isn’t visible to the outside, you can control the access to its value to make sure your object is always has a valid state.

Let’s take a look at an example to better understand the encapsulation concept.


Polymorphism defines the ability to take different forms. Polymorphism in Python allows us to define methods in the child class with the same name as defined in their parent class. In this article, we will get into the details of Polymorphism in Python in the following sequence:

What is Polymorphism?
Polymorphism in Python
Polymorphism with Function and Objects
Polymorphism with Class Methods
Polymorphism with Inheritance
What is Polymorphism?
Polymorphism is taken from the Greek words Poly (many) and morphism (forms). It means that the same function name can be used for different types. This makes programming more intuitive and easier.

In Python, we have different ways to define polymorphism. So let’s move ahead and see how polymorphism works in Python.

Polymorphism in Python
A child class inherits all the methods from the parent class. However, in some situations, the method inherited from the parent class doesn’t quite fit into the child class. In such cases, you will have to re-implement method in the child class.

There are different methods to use polymorphism in Python. You can use different function, class methods or objects to define polymorphism. So, let’s move ahead and have a look at each of these methods in detail.