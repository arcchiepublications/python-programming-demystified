try:
    # Some code that may raise exceptions
    result = 10 / 0
except (ZeroDivisionError, TypeError) as e:
    # Handling both ZeroDivisionError and TypeError
    print(f"An error occurred: {e}")
