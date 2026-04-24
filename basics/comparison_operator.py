# Compare two number: Greater, smaller, equal
a = int(input("Enter Your First Number: "))
b = int(input("Enter Your Second Number: "))

if a > b:
    print("Greater")
elif a < b:
    print("Smaller")
else:
    print("Equal")

# Check if number is even or odd
x = int(input("Enter Number: "))
if x % 2 == 0:
    print("This is Even Number: ", x)
else:
    print("This is Odd Number: ", x)
