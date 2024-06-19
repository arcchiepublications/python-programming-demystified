def countdown(number):
    while number > 0:
        yield number
        number -= 1

# Example usage
for count in countdown(3):
    print(count)
