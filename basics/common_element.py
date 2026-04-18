# Find common element from lists

list1 = [1, 2, 13, 3, 4, 5, 17]
list2 = [8, 4, 6, 1, 19, 3, 12]

# Method: Using for loop
common = []
for i in list1:
    if i in list2:
        common.append(i)

print("Common element: ", common)
