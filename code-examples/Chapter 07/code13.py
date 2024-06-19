def read_large_file(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            yield line.strip()

# Example usage
for line in read_large_file('large_file.txt'):
    # process the line
    pass
