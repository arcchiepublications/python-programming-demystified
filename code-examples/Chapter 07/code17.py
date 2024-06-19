def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Example usage
for num in fibonacci():
    if num > 10000: break
    print(num)
