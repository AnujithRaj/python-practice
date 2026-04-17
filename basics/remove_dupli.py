d = [1, 2, 2, 3, 4, 4, 5]

# Method: Using Loops
unique = []
for i in d:
    if i not in unique:
        unique.append(i)

print("Unique list:", unique)
