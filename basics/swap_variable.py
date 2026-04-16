# This function demonstrates how to swap the values of two variables using a temporary variable.
def swap_numbers():
    a = 5
    b = 10
    # Print the original values of a and b
    print("Before swapping: ", a, b)
    temp = a
    a = b
    b = temp
    # Print the swapped values of a and b
    print("After swapping:", a, b)

# Call the function to see the result 
swap_numbers()
