# Create function to add two Numbers.
def add(a,b):
    return a + b

x = int(input("Enter first Number: "))
y = int(input("Enter second Number: "))

print("sum: ",add(x,y))

# Function to check Even/Odd
def num(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

num(5)
    

# function to find Factorial.
def factorial(n):
    if n < 0:
        return "Invalid Number"
    
    result = 1
    for i in range(1, n + 1):
        result = result * i

    return result

num = int(input("Enter Number: "))
print("Factorial: ", factorial(num))
    
# Function with default arguments.
def greet(name="Guest"):
    print("Hello", name)

greet("Siddharth")
greet()

# Add
def add(a, b = 5):
    print("Sum: ", a + b)

add(2,8)
add(7)


# Function returning multiple values.
def num(a,b):
    sum = a + b
    diff = a - b
    return sum, diff

result = num(30,20)
print(result)