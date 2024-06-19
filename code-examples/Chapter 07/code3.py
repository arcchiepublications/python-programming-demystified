def simple_counter(max):
    count = 0
    while count < max:
        yield count
        count += 1

# Example usage
for i in simple_counter(3):
    print(i)
