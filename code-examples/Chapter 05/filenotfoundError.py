try:
    with open('non_existent_file.txt', 'r') as f:
        content = f.read()
except FileNotFoundError as e:
    print("FileNotFoundError:", e)
