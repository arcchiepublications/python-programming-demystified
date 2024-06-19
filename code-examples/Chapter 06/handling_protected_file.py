try:
    with open('protected_file.txt', 'w') as file:
        file.write("Some data")
except PermissionError:
    print("You do not have permission to write to this file.")
