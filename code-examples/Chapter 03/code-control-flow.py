def main():
    while True:
        print("Select a control statement:")
        print("1. If statement")
        print("2. For loop")
        print("3. While loop")
        print("4. Break statement")
        print("5. Continue statement")
        print("6. Pass statement")
        print("Press 'x' to exit")

        choice = input("Enter your choice: ")

        if choice == 'x':
            print("Exiting program...")
            break
        elif choice == '1':
            # If statement
            num = int(input("Enter a number: "))
            if num > 0:
                print("Number is positive")
            elif num < 0:
                print("Number is negative")
            else:
                print("Number is zero")
        elif choice == '2':
            # For loop
            fruits = ["apple", "banana", "cherry"]
            for fruit in fruits:
                print(fruit)
        elif choice == '3':
            # While loop
            count = 0
            while count < 5:
                print("Count:", count)
                count += 1
        elif choice == '4':
            # Break statement
            for i in range(5):
                if i == 3:
                    break
                print(i)
        elif choice == '5':
            # Continue statement
            for i in range(5):
                if i == 2:
                    continue
                print(i)
        elif choice == '6':
            # Pass statement
            for i in range(5):
                if i == 2:
                    pass
                else:
                    print(i)
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
