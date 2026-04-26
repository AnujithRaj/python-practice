# Check if Element exists in List.
lis = ["Apple", "Banana", "Mango", 20, 30, 11, "True", False, True]
item = input("Enter element to search in list: ")

if item.capitalize() in lis:
    print("Element Exist in List")
else:
    print("Does not Exist in List")


# Check if Character exists in String.
str1 = "Siddharth"
char = input("Enter character to search: ")
if char.lower() in str1.lower():
    print("Character Exist in String: ")
else:
    print("Character Does not Exist in String:")
