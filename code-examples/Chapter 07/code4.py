def fibonacci_sequence(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# Example usage
for fib in fibonacci_sequence(5):
    print(fib)
