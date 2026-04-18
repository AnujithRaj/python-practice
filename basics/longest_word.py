# This code finds the longest word in a given string.

# Define the string
fav = "I Love Python Programming"
words = fav.split()

# Method 1: Using max() function
longest_word = max(words, key=len)
print("The longest word is: ", longest_word)

# Method 2: Using for loop
longest = words[0]
for i in words:
    if len(i) > len(longest):
        longest = i

print("The longest word is: ", longest)
