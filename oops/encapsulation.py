# Create Account with private balance and getter
class Account:
    def __init__(self,name,account_num,balance):
        self.name = name
        self._account_num = account_num   # protected
        self.__balance = balance    # private

    def get_balance(self):
        return self.__balance
    
ac1 = Account("Siddharth", "7061095", 80000)

print(ac1.get_balance())


# Add deposit method with validation
class Bank:
    def __init__(self, name, account_num, balance):
        self.name=name
        self._account_num=account_num
        self.__balance=balance

    def deposit(self,amount):
        # Validation
        if not isinstance(amount,(int, float)):
            return "Amount must be a number"
        
        if amount <= 0:
            return "Invalid amount"
        
        self.__balance += amount
        return f"Deposit Successful. Current Balance: {self.__balance}"

obj1=Bank("Anujith", "844948", 879493)

print(obj1.deposit(5000))


# Add withdraw with insufficient check
class SavingAccount:
    def __init__(self,name,account_num,balance):
        self.name=name
        self._account_num=account_num
        self.__balance=balance

    def withdraw(self,amount):
        if amount > self.__balance:
            return "Insufficient Balance"
        
        self.__balance -= amount
        return f"Remaining Balance: {self.__balance}"
    
account1=SavingAccount("Siddharth", "9585949", 60000)

print(account1.withdraw(50000))


# Hide salary in Employee and return yearly salary
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary

    def details(self):
        return self.__salary * 12
    
emp1=Employee("Priti", 60000)

print(emp1.details())


# Create Student with private marks
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.__marks=marks

    def details(self):
        return self.__marks
    
stud1=Student("Shubham", 92)

print(stud1.details())


# Add method to update marks safely
class StudentMarks:
    def __init__(self,name,marks):
        self.name=name
        self.__marks=marks

    # getter method
    def get_marks(self):
        return self.__marks
    
    # Setter method
    def set_marks(self,new_marks):
        if 0 <= new_marks <= 100:
            self.__marks = new_marks
        else:
            return "Invalid marks!"
        
# Object Creation
stud1 = StudentMarks("Siddharth", 91)

# update marks
stud1.set_marks(96)

print(stud1.get_marks())


# Create Wallet with private money
class Wallet:
    def __init__(self,id_card,money):
        self.id_card=id_card
        self.__money=money

    def get_balance(self):
        return self.__money
    
person1=Wallet("Hritik", 10000)

print(person1.get_balance())


# Prevent negative transactions
class BankAccount:
    def __init__(self,name,ac_num,balance):
        self.name=name
        self._ac_num=ac_num
        self.__balance=balance

    def Transaction(self,withdraw):
        # Prevent negative or zero withdrawal
        if withdraw <= 0:
            return "Invalid Trannsaction Amount"
        # Check Insufficient balance
        if withdraw > self.__balance:
            return "Insufficient Balance"
        
        
        # Deduct Amount
        self.__balance -= withdraw
        return f"Remaining Balance: {self.__balance}"
        
ac1 = BankAccount("Siddharth","4985959",8494484)

print(ac1.Transaction(20000))
print(ac1.Transaction(-500))


# Add method to transfer money 
class CurrentAccount:
    def __init__(self,name,accountNumber,balance):
        self.name=name
        self._accountNumber=accountNumber
        self.__balance=balance

    # Controlled balance access
    def get_balance(self):
        return self.__balance

    # Transfer money to another bank account
    def transfer(self,receiver,amount):

        if amount <= 0:
            return "Invalid Amount"
        
        if amount > self.__balance:
            return "Insufficient Balance"
        
        # Deduct from sender
        self.__balance -= amount
        
        # Add to receiver
        receiver.__balance += amount

        return (
            f"Transfer Successful!\n"
            f"{self.name} Balance: {self.__balance}\n"
            f"{receiver.name} Balance: {receiver.__balance}"
        )

# Creating Account   
acc1=CurrentAccount("Komal","39849843",449339)
acc2 = CurrentAccount("Rahul", "98765432", 50000)

# Transfer money
print(acc1.transfer(acc2,20000))

# Checking Balance
print("Komal Balance: ", acc1.get_balance())
print("Rahul Balance: ", acc2.get_balance())

