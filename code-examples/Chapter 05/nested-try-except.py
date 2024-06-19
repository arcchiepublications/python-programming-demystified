try:
    # Outer try block
    num1 = int(input("Enter a dividend: "))
    num2 = int(input("Enter a divisor: "))
    
    try:
        # Inner try block
        result = num1 / num2
        print("Result:", result)
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except ValueError:
        print("Please enter valid numbers.")
    
except Exception as e:
    print("An error occurred:", e)
