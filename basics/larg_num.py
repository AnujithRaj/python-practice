# This program calculates the second largest number
num1 = list(map(int, input("Enter the list of numbers: ").split()))

largest = num1[0]
second_largest = num1[0]
for i in num1:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i

print("The second largest number is: ", second_largest)
