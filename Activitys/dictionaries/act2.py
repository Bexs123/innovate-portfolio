#Make a countries dictionary - represent countries and their capital cities

countries = {
    "United Kingdom":"London",
    "France":"Paris",
    "Germany":"Berlin",
    "Spain":"Madrid",
    "Italy":"Rome"
}

# print(countries["United Kingdom"])

#Used the .setdefault() method to add any 2 more countries and capitals of my choice

countries.setdefault("New Zealand", "Wellington")
countries.setdefault("New Jersey","Trenton")

# print(countries["New Zealand"])

#Testing the .updated() method too

countries.update({"Australia":"Canberra"})
countries.update({"Southern Ireland":"Dublin"})

#List() method
print(list(countries.keys()))

#For Loop to iterate through the countries
for i in countries.keys():
    print(i)
    
    
#Print all items using a method previously seen before.
#Make a note of which method you prefer, and why.

# I prefer the for loop because it is much cleaner and faster to write, the trouble with the list method is that you may forget how many brackets to use or you may miss the list off

#You've had a change of heart - now update all the values with the main language spoken in the countries instead of capitals