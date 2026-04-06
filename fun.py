import os

answer = input("Do you love me? (yes or no): ")

if answer.lower() == "yes":
    print("Awww 💖 you're the best!")
else:
    import os
    file_path = "C:\\Users\\Admin\\Desktop\\Love.py"  # Change this to the actual path of your Love.py file

    try:
        os.remove(file_path)
        print("File deleted successfully!")
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")
 