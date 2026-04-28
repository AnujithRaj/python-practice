# Print numbers until user enters 0.
while True:
    num = int(input("Enter Number:"))
    
    if num == 0:
        break
    print(num)

# Guess the number game.
guess = 11
while True:
    num = int(input("Enter Number:"))
    
    if num < guess:
        print("Too Low")
    elif num > guess:
        print("Too High")
    else:
        print("Correct")
        break

# Print multiplication table.
table = int(input("Enter Table:"))
i = 1
while i <= 10:
    print(f"{table} * {i} = {table * i}")
    i +=1


    
