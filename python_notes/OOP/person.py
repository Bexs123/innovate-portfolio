# keyword class is used to define a new class
# This is to distinguish classes from regular functions
class Person():
    
# This is called a constructor or an initaliser, bascially it just tells Python how to create an object of this class.
# self is one of the constructor's parameters, it is a default that is created with all classes, it allows us to go onto make objects from this class
    def __init__(self, person_name, person_age, person_height):
        
# This is a attribute of the class
        self.name = person_name
        self.age = person_age
        self.height = person_height
        
# setter - set the value of one of the objects's attributes using a method
# A function in an object is a method
# person_hair is the characteristic or attribute that has been set
    def set_hair(self, person_hair):
        self.hair = person_hair
        
# getters
    def get_hair(self):
        print(self.hair)

        
        
        
       
        

        
        
#         self.name = person_name
#         self.employer = 'Code Nation'
#         self.age = age
#         self.loves_metal = True

# Instances of person
# Will = Person()
# It will give an error, because it hasn't be given a person name  

# instructor_one = Person('Will', 31) 
# instructor_two = Person('Katy', 30)   

# print(instructor_one.name)
# print(instructor_one.employer)
# print(instructor_one.loves_metal)

# print(instructor_two.name)
# print(instructor_two.employer)