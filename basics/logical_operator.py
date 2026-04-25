age = int(input("Enter age: "))
citizen = input("Enter nationality: ").strip().lower()

# AND Operator
if age >= 18 and citizen == "indian":
    print("Eligible for Voting")
else:
    print("Not Eligible")

# OR Operator
print("\nUsing OR condition:")
if age >= 18 or citizen == "indian":
    print("Eligible")
else:
    print("Not Eligible")
