# Find Second Largest Number in List.
list1 = list(map(int, input("Enter Numbers: ").split()))

list1 = list(set(list1))    # remove duplicate
list1.sort()

if len(list1) < 2:
    print("No Second Largest")
else:
    print("Second Largest: ", list1[-2])
