# Count the number of vowels in a given string
s = "Hello, World!"
vowels = "aeiouAEIOU"
count = [0]

# Method: Using for loop
for i in s:
    if i in vowels:
        count[0] += 1
print("Number of vowels in the string: ", count[0])
