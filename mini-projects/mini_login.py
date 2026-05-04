# Build mine login system using dictionary.

users = {
    "anujith": "70249",
    "admin": "admin1234"
}

while True:
    print("/n1.Login")
    print("2. Register")
    print("3. Exit")

    choice = input("Enter choice: ")

    # Login
    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in users and users[username] == password:
            print("Login sucessful ✅")
        else:
            print("Invalid username or password ❌")

    # Register
    elif choice == "2":
        username = input("Create username: ")

        if username in users:
            print("User already exists ❌")
        else:
            password = input("Create password: ")
            users[username] = password
            print("Registration sucessful ✅")

    # Exit
    elif choice == "3":
        print("Goodbye 👋")
        break
    else:
        print("Invalid choice ❌")