# Merging two list in Python
lis1 = [1, 2, 3]
lis2 = [4, 5, 6]

# Method: Using + Operator
merged_list = lis1 + lis2
print("Merged List: ", merged_list)

# Method: Using extend() method
# lis1.extend(lis2)
# print("Merged List: ", lis1)

# Method: Using Loops
merged_list = []
for i in lis1:
    merged_list.append(i)
for i in lis2:
    merged_list.append(i)
print("Merged List: ", merged_list)
