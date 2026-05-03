# Create a class Student
    # attributes: name, age
    # method: display()
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(self.name,self.age)

student1=Student("Siddharth",22)
student2=Student("Anujith",24)

student1.display()
student2.display()


