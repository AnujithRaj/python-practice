# Stop Loop when Number = 5.
for i in range(20):
    num = int(input("Enter Number:"))

    if num == 5:
        break
    
    print("Number: ", num)
    

# Skip even Number.
for i in range(1,20,2):
    print("Odd Number: ",i)

# Use pass in empty loop.
for i in range(10):
    pass