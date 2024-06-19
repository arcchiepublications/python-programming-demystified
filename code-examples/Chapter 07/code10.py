def large_range(max_val):
    num = 0
    while num < max_val:
        yield num
        num += 1

# Example usage
for number in large_range(1000000):
    # process the number
    pass
