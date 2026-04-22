# String in Python
Full_name = "Anujith Raj"
# Printing the string, its type, and accessing individular characters using their index, where the index starts from 0.
print(Full_name)
print(type(Full_name))
print(Full_name[0])  # Accessing the first character
print(Full_name[1])  # Accessing the second character
print(Full_name[6])  # Accessing the seventh character

# This Program Count the Number of Vowels in a string.
str1 = "Siddharth"
count = 0
for i in str1:
    if i in "aeiouAEIOU":
        count += 1

print("Vowels in String", count)

# Reverse a String
print("Original String: ", str1)

revs = ""
for i in str1:
    revs = i + revs
print("Reverse String: ", revs)

# Check Palindrome.
str2 = "Ladale"

if str2.lower() == str2[::-1].lower():
    print("Palindrome")
else:
    print("Not Palindrome")

# Convert string to Uppercase/Lowercase
str3 = "upper"
upper_str = str3.upper()
print("Uppercase: ", upper_str)

lower_str = str3.lower()
print("Lowercase: ", lower_str)
