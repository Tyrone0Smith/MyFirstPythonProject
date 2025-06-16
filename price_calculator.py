# This is a product dictionary that contains product names as keys and their prices as values.
products = {
    "apple": 0.50,
    "banana": 0.30,
    "orange": 0.80,
    "grape": 1.20,
    "kiwi": 1.50
}

while True:
    product_name = input("Enter the product name (or 'exit' to quit): ").strip().lower()

    if product_name == 'exit':
        print("Exiting the program.")
        break # Exit the while loop

    if product_name in products:
        price = products[product_name]

        # --- ADDED: try-except block for quantity input ---
        try:
            quantity_input = input(f"Enter the quantity of {product_name} (price: ${price:.2f}): ")
            quantity = int(quantity_input) # This line might cause a ValueError if input is not a number

            if quantity <= 0: # Also add a check for non-positive quantities
                print("Quantity must be a positive number. Please try again.")
                continue # Skip to the next iteration of the while loop

            total_price = price * quantity
            print(f"{quantity} {product_name}(s) @ ${price:.2f} each: Total = ${total_price:.2f}")

        except ValueError:
            # This block runs if int(quantity_input) fails
            print("Invalid quantity. Please enter a whole number.")
            continue # Skip to the next iteration of the while loop to ask for product name again
        # --- END ADDED BLOCK ---

    else:
        print("Product not found. Please try again.")
