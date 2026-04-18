# Rotate a list  in Python
list1 = [1, 2, 3, 4, 5]

# Method: Using Slicing
rotation = [list1[-1]] + list1[:-1]
print("Rotated List: ", rotation)

# Method: Using Loops
lis = [2, 4, 9, 1, 7]
last = lis[-1]
for i in range(len(lis) - 1, 0, -1):
    lis[i] = lis[i - 1]

lis[0] = last

print("Rotated List: ", lis)
