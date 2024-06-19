# Get input from the user
number = int(input("Enter a number: "))

# Check if the number is positive, negative, or zero
if number >= 0:
    # Check if the number is positive
    if number > 0:
        print("The number is positive.")
    # If the number is not positive, it must be zero
    else:
        print("The number is zero.")
else:
    print("The number is negative.")
