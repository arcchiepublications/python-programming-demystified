# Reading a text file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Writing to a text file
with open('newfile.txt', 'w') as file:
    file.write("Writing new content.")
