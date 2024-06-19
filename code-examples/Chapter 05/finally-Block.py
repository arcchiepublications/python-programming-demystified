try:
    # Code that may raise an exception
    x = 1 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This will always execute, regardless of exceptions.")
