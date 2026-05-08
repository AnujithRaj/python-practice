# Create a class Car with brand and model, print details.
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def details(self):
        return f"Brand: {self.brand}, Model: {self.model}"
       
car1=Car("BMW", "M3")
car2=Car("Audi", "A6")

print(car1.details())   
print(car2.details())

# Create a class Student with name, marks, display method
class Student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
        
    def display(self):
        return f"Name: {self.name}, Marks: {self.marks}"
    
student1=Student("Siddharth", 98)
student2=Student("Anujith", 96)


print(student1.display())
print(student2.display())


#  Create multiple objects of Boook and print titles.
class Book:
    def __init__(self, name):
        self.name=name

    def titles(self):
        return f"Title: {self.name}"
    
book1=Book("Success")
book2=Book("Atomic Habits")

print(book1.titles())
print(book2.titles())


# Create a class Circle with radius and method to calculate area.
class Circle:
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return 3.14 * (self.radius ** 2)
    
obj1 = Circle(10)
obj2 = Circle(21)

print("Area: ", obj1.area())
print("Area: ", obj2.area())


# Create a class Employee with name and salary.
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    def display(self):
        return f"Name: {self.name}, Salary: {self.salary}"
    
emp1=Employee("Priti", 80000)
emp2=Employee("Komal", 60000)

print(emp1.display())
print(emp2.display())

# Create a class Laptop with price, apply discount.
class Laptop:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price

    def apply_discount(self,percent):
        self.price = self.price - (self.price * percent / 100)
        return self.price
    
obj1=Laptop("HP", 60000)
obj2=Laptop("Dell", 80000)

print(obj1.apply_discount(10))
print(obj2.apply_discount(15))

# Create a class Mobile with brand and price.
class Mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price

    def display(self):
        return f"Brand: {self.brand}, Price: {self.price}"
    
obj1=Mobile("Apple",80000)
obj2=Mobile("Oppo",60000)

print(obj1.display())
print(obj2.display())



# Create a class Person and print details.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def details(self):
        return f"Name: {self.name}, Age: {self.age}"
    
person1=Person("Shubham", 23)
person2=Person("Komal", 21)

print(person1.details())
print(person2.details())



# Create a class Dog with name and sound method.
class Dog:
    def __init__(self,name,sound):
        self.name=name
        self.sound=sound

    def bark(self):
        return f"Name: {self.name}, Sound: {self.sound}"
    
dog1=Dog("Pommy", "Bhoo-Bhoo")
dog2=Dog("Tommy", "Boo-Boo")

print(dog1.bark())
print(dog2.bark())

# Create a class Movie with title and rating.
class Movie:
    def __init__(self,title,rating):
        self.title=title
        self.rating=rating

    def details(self):
        return f"Title: {self.title}, Rating: {self.rating}"
    
movie1=Movie("3 Idiots", 7.8)
movie2=Movie("Dangal", 8.4)

print(movie1.details())
print(movie2.details())
    