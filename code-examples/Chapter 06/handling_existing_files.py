import os

filename = "existing_file.txt"
try:
    if os.path.exists(filename):
        raise FileExistsError("File already exists")
    with open(filename, 'w') as file:
        file.write("Some data")
except FileExistsError as e:
    print(e)
