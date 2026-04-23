# Create a Dictionary of student info.
student = {"name": "Anujith", "age": 22, "city": "Rajgit"}
print("Student: ", student)

# Add a new Key_Value pair.
student["course"] = "Data Science"
print("Student After new Key Value:", student)

# Update a Value.
student["name"] = "Anujith Raj"
print("Updated Value: ", student["name"])

# Print all keys and values.
print("All Keys and Value: ", student)

# Check if a key exists.
if "age" in student:
    print("Age Key exists in student")
else:
    print("Age key not found")
