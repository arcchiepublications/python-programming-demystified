# Writing to a file
with open('example_to_write.txt', 'w') as file:
    file.write("Hi, Python!")
# Appending to a file
with open('example_to_write.txt', 'a') as file:
    file.write("\nAppending a new line to existing file.")
