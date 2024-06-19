numbers = [1, 2, 3, 4, 5]
it = iter(numbers)

try:
    while True:
        print(next(it))
except StopIteration:
    pass
