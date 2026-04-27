# Compare two lists using is and ==
lis1 = [2,3,4,5,6]

# Case 1: Same reference
lis2 = lis1

print("Using 'is' (same object):", lis1 is lis2)
print("Using '==' (same value):", lis1 == lis2)


# Case 2: Different object, same value
lis3 = [2,3,4,5,6]

print("Using 'is' (different object):", lis1 is lis3)
print("Using '==' (same value):", lis1 == lis3)

# Understanding
# is : Same memory
# == : Same Value