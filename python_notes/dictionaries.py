print("this is dictionaries")

my_cat = {"name":"Salem",
          "colour": "black",
          "mood":"sassy"
          }


my_dog = {
        "name":"Lexi",
        "colour":"Brindle",
        "mood":"Lazy"
          } 

print(my_dog["name"])
print(my_dog["colour"])

#Using methods to identify dictionary items

#Dot notation
# print(my_dog.keys())

x =my_dog.keys()

my_dog["age"]=2

print(x)


print(my_dog.values())
print(my_dog.items())
print(my_dog.get("mood"))

#casuses an error
# print(my_dog["mood"])

print(my_dog.get("legs", "This key doesn't exist"))

print(my_dog.keys())
print(list(my_dog.keys()))

#Using for loops to make it better
for i in my_dog.keys():
    print(i)
    
#Set a new key:value using .setdefault()
my_dog.setdefault("hungry", True)

#You can't use it to update an existing key
my_dog.setdefault("mood", "sleepy")

#Update - update extising key values - add new key values
my_dog.update({"legs":"4"})
print(my_dog)

#remove key values by using .pop
my_dog.pop("mood")
print(my_dog)
