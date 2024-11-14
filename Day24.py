# OOP (object oriented programming)
# It is way of programming.
# Class and Objects (Basic)
# Class (it is a blue print used to create objects and to define objects)
# Objects (It is created through class and we use it to do most of the things in our program) 
# Done by Abhiyan Shrestha

class car:
    name = 'honda' # attributes
    max_speed = '400Km/Hr' # attributes
    price = '2M' # attributes

car1 = car() # car1 is object of car if we call car class
car1.name = 'ferrari'
car2 = car() # car2 is object of car if we call car class

print(car1.name,car1.max_speed,car1.price)
print(car2.name,car2.max_speed,car2.price)

a = 'hello'
b = a.upper()
print(b)

class cars:
    name = 'honda' # attributes
    max_speed = '400Km/Hr' # attributes
    price = '2M' # attributes

    def get_max_speed(self):
        print(self.max_speed)
    
    def set_max_speed(self,max_speed): # to change the value of the max speed this function is made
        self.max_speed = max_speed
        

cars1 = cars()
cars2 = cars()

cars1.set_max_speed('300 Km/Hr')

cars1.get_max_speed()

# Python OOPs Concepts
# Done by Abhiyan Shrestha

##########################
# Polymorphism

def add(x, y, z = 0):
    return x + y + z

print(add(2,3))
print(add(2,3,4))

class Nepal():
    def capital(self):
        print('Kathmandu is capital of Nepal')

    def language(self):
        print('Nepali is national language')
    
    def type(self):
        print('Nepal is a developing country')

class Usa():
    
    def capital(self):
        print('Washinton Dc is capital of usa')
    
    def language(self):
        print('English is national language')

    def type(self):
        print('America is a developed country')

obj_nepal = Nepal()
obj_usa = Usa()

for country in (obj_nepal, obj_usa):
    country.capital()
    country.language()
    country.type()
###########################
# Inheritance

class Person(object):
    # Constructor
    def __init__(self,name,id):
        self.name = name
        self.id = id
    
    # To check if this person is an employee
    def Display(self):
        print(self.name,self.id)

# Driver Code
emp = Person('Abhiyan', 102) # An Object of person
emp.Display()

#############################
# Abstract

from abc import ABC, abstractmethod

class Polygon(ABC):

    @abstractmethod
    def noofsides(self):
        pass

class Triangle(Polygon):
    # Overriding abstract method 
    def noofsides(self):
     print('I have 3 sides')

class Pentagon(Polygon):
    # overriding abstract method
    def noofsides(self):
        print('I have 5 sides')

class Hexagon(Polygon):
    # overriding abstract method
    def noofsides(self):
        print('I have 6 sides')

class Quadrilateral(Polygon):
    # overriding abstract method
    def noofsides(self):
        print('I have 4 sides')

# Driver Code
R = Triangle()
R.noofsides()

K = Quadrilateral()
K.noofsides()

R = Pentagon()
R.noofsides()

K = Hexagon()
K.noofsides()

########################################
# Encapsulation

class Base:
    def __init__(self):
        # protected member
        self._a = 2

# Creating a derived class
class Derived(Base):
    def __init__(self):
        # calling the constructor of 
        # Base Class
        Base.__init__(self)
        print('Calling modified protected number of base class: ',  self._a)

        # Modify the protected variable
        self._a = 3
        print('Calling modified protected member outside class: ', self._a)

obj1 = Derived()
obj2 = Base()

# Calling protected member
# can be accessed but should not be done due to convention
print('Accessing protected number of obj1: ', obj1._a)

# Accessing the protected variable outside
print('Accessing protected numbe of obj2: ',obj2._a)












