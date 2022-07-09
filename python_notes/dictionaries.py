print("Python Dictionaries")
print("This is my Python Notes and Examples for Dictionaries")

# They store data for us in a really specific way.
# Just like actual dictionaries, you can look things up, however they're not in alphabetical order.
# They are more like lists they store multiple values, we use {} to define our dictionaries.

# Example of List
my_cat = ["Salem", "black", "sassy"]

# Example of Dictionary - name, colour, mood are all keys, and the values are Salem, black, sassy
my_cat = {
          "name": "Salem", 
          "colour": "black",
          "mood": "sassy"
          }

# Unlike lists, they use key:value pairs, so you can give each element a name.

# Dictionaries do not have a numbered index. So you have to use a different method to extract or change values.

# My Dictionary for my pet dog
my_dog = {
          "name": "Lexi", 
          "colour": "Brindle", 
          "mood": "Lazy"
          }

print(my_dog[2])  # in <module> print(my_dog[2]) KeyError: 2

print(my_dog["name"])
print(my_dog["colour"])

print(my_dog.get("age", "Error"))  # Answer Error

# You can change a value of an existing key
my_cat["name"] = "Whiskers"
print(my_cat["name"])

# Using methods to identify dictionary items
# .keys(), .values(), .items(), .get()

# print(my_cat.keys()) - dict_keys(['name', 'colour', 'mood'])

# print(my_cat.values()) - dict_values(['Salem', 'black', 'sassy'])

# print(my_cat.items()) - dict_items([('name', 'Salem'), ('colour', 'black'), ('mood', 'sassy')])

# print(my_cat.get("name")) - Salem

# You can make the output look a little bit cleaner by using the list() method

print(list(my_dog.keys()))
print(list(my_dog.values()))
print(list(my_dog.items()))

# Dot notation
# print(my_dog.keys())

x = my_dog.keys()

my_dog["age"] = 2

print(x)

print(my_dog.values())
print(my_dog.items())
print(my_dog.get("mood"))

print(my_dog.get("legs"))  # causes an error
print(my_dog.get("legs", "This key doesn't exist"))  # You can add an error message
print(my_dog.keys())
print(list(my_dog.keys()))

# To make the output better and clearner, incorporate for loops 
for i in my_dog.keys():
    print(i)

# Set a new key:value using .setdefault()
my_dog.setdefault("hungry", True)

# You can't use it to update an existing key
my_dog.setdefault("mood", "sleepy")

# Update - update extising key values - add new key values
my_dog.update({"legs": "4"})
print(my_dog)

# Remove keys from a dictionary using .pop()method
my_dog.pop("mood")
print(my_dog)

# del method - lets you specify which key to delete
my_cat = {"name": "Salem", "colour": "black", "mood": "sassy"}
del my_cat["mood"]
print(my_cat)  # deletes the key:value mood: sassy