def flatten(nested_list):
    for sublist in nested_list:
        for item in sublist:
            yield item

# Example usage
nested_list = [[1, 2, 3], [4, 5], [6]]
for number in flatten(nested_list):
    print(number)
