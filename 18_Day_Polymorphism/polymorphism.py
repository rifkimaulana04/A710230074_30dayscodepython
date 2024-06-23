# Konsep Polymorphism

# contoh penggunaan duck typing
def print_all(items):
    for item in items:
        print(item)
# list
my_list = [1, 2, 3]
# tuple
my_tuple = (4, 5, 6)
# string
my_string = "Hello, world!"

# memanggil fungsi print_all dengan parameter my_list, my_tuple, dan my_string
print_all(my_list) # output: 1 2 3
print_all(my_tuple) # output: 4 5 6
print_all(my_string) # output: H e l l o , w o r l d !

# Polymorphism pada OOP

class India():
    def capital(self):
        print("New Delhi is the capital of India.")
    
    def language(self):
        print("Hindi is the most widely spoken language of India.")
    
    def type(self):
        print("India is a developing country.")

class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")

obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country

# Polymorphism pada OOP

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# membuat objek rectangl
my_rectangle = Rectangle(5, 6)

# memanggil method area pada objek rectangle
result1 = my_rectangle.area()
print(result1) # output: 30

# membuat objek circle
my_circle = Circle(7)

# memanggil method area pada objek circle
result2 = my_circle.area()
print(result2) # output: 153.86

# Polymorphism pada OOP

class Dog():
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(self.name, 'says bark, bark, bark!')

class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, 'says meeeoooow')

class Bird():
    def __init__(self, name):
        self.name = name    
    
    def speak(self):
        print(self.name, 'says tweet')

oDog1 = Dog('Rover')
oDog2 = Dog('Fido')
oCat1 = Cat('Fluffy')
oCat2 = Cat('Spike')
oBird = Bird('Big Bird')

petsList = [oDog1, oDog2, oCat1, oCat2, oBird]

for oPet in petsList:
    oPet.speak