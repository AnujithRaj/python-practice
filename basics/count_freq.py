num = [1, 2, 2, 3, 4, 4, 5]

# Method: Using Loops
freq = {}
for i in num:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print("Frequency of elements:", freq)
