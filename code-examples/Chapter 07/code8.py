def accumulator():
    total = 0
    while True:
        value = yield total
        if value is None: break
        total += value

# Example usage
acc = accumulator()
next(acc)  # Start the generator
print(acc.send(1))  # Send a value and print the total
print(acc.send(2))
