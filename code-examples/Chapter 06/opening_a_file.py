# Opening a file
file = open('example_to_read.txt', 'r')  # Open a file in read mode
content = file.read()  # Read the content of the file
file.close()  # Always close the file

print(content)
