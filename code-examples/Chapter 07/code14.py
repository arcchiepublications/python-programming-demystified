def read_log_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

# Example usage
for log_line in read_log_file('server.log'):
    # Process each log line
    pass
