# This is a basic Product class, focusing on core OOP concepts.
class Product:
    def __init__(self, name, price, stock): # Changed 'quantity' to 'stock' as per previous task
        self.name = name
        self.price = price
        self.stock = stock # 'stock' represents available units, not quantity bought

    # Method to get product details
    def get_details(self):
        return f"Product: {self.name}, Price: ${self.price:.2f}, Stock: {self.stock} units."

    # Method to update stock (add or remove)
    def update_stock(self, quantity_change):
        self.stock += quantity_change
        if self.stock < 0:
            print(f"Warning: Stock for {self.name} cannot be negative! Current stock: {self.stock}")
            # Optional: self.stock = 0 # You could reset to 0 here if stock should never go below zero
        print(f"Stock for {self.name} updated to {self.stock}.")

    # You can keep the __str__ and __repr__ from your original code if you like,
    # as they are very useful for printing objects.
    def __str__(self):
        return f"Product(name={self.name}, price={self.price}, stock={self.stock})"
    def __repr__(self):
        return f"Product(name={self.name!r}, price={self.price!r}, stock={self.stock!r})"
 # --- Creating Product Objects (Instances) ---
print("--- Creating Products ---")
laptop = Product("Laptop", 1200.00, 10) # 10 units in stock
mouse = Product("Mouse", 25.00, 50)    # 50 units in stock
keyboard = Product("Mechanical Keyboard", 75.50, 15) # Your third product!

# --- Getting initial details ---
print("\n--- Initial Product Details ---")
print(laptop.get_details())
print(mouse.get_details())
print(keyboard.get_details())

# --- Updating stock and re-checking details ---
print("\n--- Updating Stock ---")
laptop.update_stock(5)      # Add 5 to laptop stock
mouse.update_stock(-20)     # Sell 20 mice

print("\n--- Testing Negative Stock Scenario ---")
keyboard.update_stock(-20) # Try to sell more than available (15 - 20 = -5)

print("\n--- Updated Product Details ---")
print(laptop.get_details())
print(mouse.get_details())
print(keyboard.get_details())   