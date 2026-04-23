# Create a Set with duplicate values
set1 = {9, 5, 3, 4, 6, 7, 9, 3, 5, 3}
print("Set: ", set1)  # Duplicates removed automatically

# Add Element
set1.add(20)
print("Set After Add Element: ", set1)

# Remove Element
set1.remove(6)
print("Set After Remove Element: ", set1)

# Create Second Set
set2 = {6, 2, 8, 7, 5, 7}
# Perform Uinion
print("Union: ", set1 | set2)
print("Union (Method)", set1.union(set2))

# Perform Intersection
print("Intersection: ", set1 & set2)
print("Intersection (Method): ", set1.intersection(set2))
