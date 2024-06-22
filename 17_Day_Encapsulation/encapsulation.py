# Implementasi Private Variabel

class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

car = Car("Honda", "Civic", 2022)
print(car.get_make())
print(car.get_model())
print(car.get_year())

# Implementasi Getter dan Setter

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

person = Person("Abdul Hakim", 25)
print(person.get_name())
print(person.get_age())

person.set_name("Ryan Hakim")
person.set_age(30)

print(person.get_name())
print(person.get_age())

print(person.__name)

# Abstraction pada OOP

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)
 

s = Stack()
print(s.is_empty())

s.push(1)
s.push(2)
s.push(3)
print(s.peek())
print(s.size())

s.pop()
print(s.peek())
print(s.size())