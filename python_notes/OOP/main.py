# Import the Person class from the person.py file
from person import Person

# use the class Person to create an object called liam
liam = Person("Liam")
# liam - object we created
# Person("Liam") - Name of the person we passed to the class

old_team_leader = Person("Liam", 31, "6'7''")

will = Person("Will", 31, "6'0''")
                    
katy = Person('Katy', 30, "5'6''")

demi = Person('Dami', 29, "5'8''")

will.set_hair('Black Mullet')

will.get_hair()

demi.set_hair('red')

demi.get_hair()