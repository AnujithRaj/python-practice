# Create a Tuple of 5 elements.
tup = (95, 34, 67, 93, 53)
print("Original Tuple: ", tup)

# Tuple is immutable. You cannot change value, no add, no remove and no update.
# tup[0] = 100   # ❌ Error (tuple is immutable)

# Convert Tuple into List
lst = list(tup)
print("Converted to List: ", lst)

# Modify Converted List
lst.append(92)
print("Modified List: ", lst)

# Convert List into Tuple
tup1 = tuple(lst)
print("Converted Tuple: ", tup1)
