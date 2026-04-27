# Check if number is positive, negative, or zero.
num = int(input("Enter your number:"))
if num > 0:
    print("Positive Number:",num)
elif num < 0:
    print("Negative Number:",num)
else:
    print("zero:",num)


# Find largest of 3 numbers.
a = int(input("Enter First Number:"))
b = int(input("Enter Second Number:"))
c = int(input("Enter Third Number:"))
if a >= b and a >= c:
    print("A is Largest Number:",a)
elif b >= a and b >= c:
    print("B is Largest Number:",b)
else:
    print("C is Largest Number:")


# Grade system: 
marks = int(input("Enter your Marks:"))
if marks >= 90:
    print("Grade A:",marks)
elif marks >= 75:
    print("Grade B:",marks)
elif marks >= 60:
    print("Grade c:",marks)
elif marks >= 40:
    print("Pass:",marks)
else:
    print("Fail:",marks)
