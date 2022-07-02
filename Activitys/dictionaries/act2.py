# Make a countries dictionary - represent countries and their capital cities

countries = {
    "United Kingdom":"London",
    "France":"Paris",
    "Germany":"Berlin",
    "Spain":"Madrid",
    "Italy":"Rome"
}

print(countries) # It will show all the countries and the key pair values
print(countries["United Kingdom"]) # It will only show the ket value pair for United Kingdom

# Used the .setdefault() method to add any 2 more countries and capitals of my choice

countries.setdefault("New Zealand", "Wellington")
countries.setdefault("New Jersey","Trenton")

print(countries)
print(countries["New Zealand"])

# Testing the .updated() method too

countries.update({"Australia":"Canberra"})
countries.update({"Southern Ireland":"Dublin"})

# List() method
print(list(countries.keys())) # Using this method will only print out the keys and not there value in one line

print(list(countries.values())) # using this method will only print the values and not the keys, in this example it will print out the capitals

print(list(countries.items())) # Using this method will print out the keys and values.

# For Loop to iterate through the countries
for i in countries.keys(): # Using .keys() method it will only print the keys out and not the values - Keys will beb the countries
     print(i)
    
for i in countries.items(): # .items() method will show both key and value pair - Countries and Capitals
    print(i)

for i in countries.values(): # .values() method it will only show the values in this example it will be the Capitals
    print(i)
    
    
# Print all items using a method previously seen before.
# Make a note of which method you prefer, and why.

# I prefer the for loop because it is much cleaner and faster to write, the trouble with the list method is that you may forget how many brackets to use or you may miss the list method off

# You've had a change of heart - now update all the values with the main language spoken in the countries instead of capitals

countries.update({
    "United Kingdom":"English",
    "France":"French",
    "Germany":"German",
    "Spain":"Spanish",
    "Italy":"Italian",
    "New Zealand": "English",
    "New Jersey":"English",
    "Australia":"English",
    "Southern Ireland":"English"
    })

print(countries)