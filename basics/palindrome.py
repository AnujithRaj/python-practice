# Check if a string is a palindrome or not
p = "Ladale"
rev = ""
# Method: Using Loops
for i in p:
    rev = i + rev
if p == rev:
    print("True")
else:
    print("False")
