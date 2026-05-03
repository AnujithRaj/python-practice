# Create a class Student
    # attributes: name, age
    # method: display()
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        return f"Name: {self.name}, Age: {self.age}"

student1=Student("Siddharth",22)
student2=Student("Anujith",24)

print(student1.display())
print(student2.display())



# Create a class Dog
    # attribute: name
    # method: bark() --> print "name is barking"

class Dog:
    def __init__(self,name):
        self.name=name

    def bark(self):
        return f"{self.name} is barking"

dog1=Dog("Tommy")

print(dog1.bark())


# Create a class Rectangle
    # attributes: length, width
    # method: area(), perimeter()

class Rectangle:
    def __init__(self,length, width):
        self.length=length
        self.width=width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

rectangle1 = Rectangle(10,20)

print(rectangle1.area())
print(rectangle1.perimeter())



# Create class BankAccount
    # attribute: blance
    # method: deposit(amount), withdraw(amount), check

class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    
    def deposit(self,amount):
        if amount <= 0:
            return "Invalid amount"
        self.balance += amount
        return self.balance
    
    def withdraw(self,amount):
        if amount > self.balance:
            return "Insufficient balance"
        self.balance -= amount
        return self.balance
    
    def check(self):
        return self.balance
    
account1 = BankAccount(20000)

print("After deposit: ", account1.deposit(5000))
print("After withdraw: ", account1.withdraw(10000))
print("Current balance: ", account1.check())