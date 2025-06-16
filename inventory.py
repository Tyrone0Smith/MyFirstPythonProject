# This is a product dictionary that contains product names as keys and their prices as values.
products = {
    "apple": 0.50,
    "banana": 0.30,
    "orange": 0.80,
    "grape": 1.20,
    "kiwi": 1.50
}
# This function takes a product name as input and returns its price.
def get_product_price(product_name):
    """Returns the price of the given product."""
    return products.get(product_name, "Product not found")
# This function takes a product name and quantity as input and returns the total price.
def calculate_total_price(product_name, quantity):
    """Calculates the total price for a given product and quantity."""
    price = get_product_price(product_name)
    if isinstance(price, str):
        return price  # Return error message if product not found
    return price * quantity
# This function takes a product name and quantity, and returns a formatted string with the total price.
def format_price_message(product_name, quantity):
    """Formats a message with the product name, quantity, and total price."""
    total_price = calculate_total_price(product_name, quantity)
    if isinstance(total_price, str):
        return total_price  # Return error message if product not found
    return f"The total price for {quantity} {product_name}(s) is ${total_price:.2f}."
# This function demonstrates the usage of the above functions.
def main():
    """Main function to demonstrate product price calculations."""
    product_name = "apple"
    quantity = 3
    
    message = format_price_message(product_name, quantity)
    print(message)
if __name__ == "__main__":
    main()
# This code defines a simple inventory system that allows users to get product prices and calculate total costs.
# The product dictionary contains product names and their prices.
# The `get_product_price` function retrieves the price of a product by its name.