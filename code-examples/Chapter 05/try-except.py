try:
    # Trying to divide by zero
    result = 10 / 0
    print("This will not be printed.")
except ZeroDivisionError as e:
    # Handling the ZeroDivisionError
    print("Caught an exception:", e)

print("Program continues here.")
