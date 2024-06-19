def read_lines(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

# Example usage
for line in read_lines('example.txt'):
    print(line)
