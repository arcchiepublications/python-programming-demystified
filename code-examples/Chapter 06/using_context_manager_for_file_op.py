# Using context manager for file operations
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())
