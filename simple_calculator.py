# This is a simple calculator that allows the user to perform basic arithmetic operations.

print("--- Simple Interactive Calculator ---")

while True:
    try:
        # Get user input for numbers
        num1_str = input("Enter first number: ")
        num2_str = input("Enter second number: ")

        # Convert inputs to float (allows for decimal numbers)
        num1 = float(num1_str)
        num2 = float(num2_str)

        # Perform calculations
        result_add = num1 + num2
        result_sub = num1 - num2
        result_mul = num1 * num2

        # Handle division by zero
        if num2 == 0:
            result_div = "Undefined (cannot divide by zero)"
        else:
            result_div = num1 / num2

        # Display results
        print("\nResults:")
        print("Addition:", result_add)
        print("Subtraction:", result_sub)
        print("Multiplication:", result_mul)
        print("Division:", result_div) # This will print "Undefined" or the number

    except ValueError:
        # Catch errors if the user enters non-numeric input
        print("Invalid input. Please enter numbers only.")
        # 'continue' here would skip the 'another' prompt and ask for numbers again.
        # But we want to ask if they want to try again or exit.

    # Ask if the user wants to perform another calculation
    while True: # This inner loop is for validating the 'yes/no' input
        another = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
        if another == 'yes':
            break # Break out of this inner loop to go back to the start of the main calculator loop
        elif another == 'no':
            print("Thank you for using the calculator!")
            exit() # Exit the entire program
        else:
            print("Invalid input, please enter 'yes' or 'no'.")

# End of the calculator program