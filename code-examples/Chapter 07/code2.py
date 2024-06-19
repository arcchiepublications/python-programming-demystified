def reverse_string(string):
    length = len(string)
    for i in range(length - 1, -1, -1):
        yield string[i]

# Example usage
for char in reverse_string("hello"):
    print(char)
