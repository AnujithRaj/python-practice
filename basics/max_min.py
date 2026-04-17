lst = [10, 20, 5, 15, 30]

# Finding the maximum and minimum values in the list
max_value = max = lst[0]  # Initialize max to the first element of the list
min_value = min = lst[0]  # Initialize min to the first element of the list

for i in lst:
    if i > max_value:
        max_value = i
    if i < min_value:
        min_value = i

print("max: ", max_value)
print("min: ", min_value)
