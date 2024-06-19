try:
    # Code that may raise exceptions
    x = int(input("Enter a number: "))
    y = 10 / x
    print("Result:", y)
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero. Please enter a non-zero number.")
except Exception as e:
    print("An error occurred:", e)
