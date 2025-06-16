# This is a Python script that first writes data to a file and then reads it back, demonstrating file I/O operations.
import json
# Sample data to write to a file
data_to_write = {
    "name": "Alice",
    "age": 20,
    "grade": "A",
    "subjects": ["Math", "Science", "English"],
    "attendance": 95
}
# Specify the file name
file_name = "student_data.json"
# Write data to the file
with open(file_name, 'w') as file:
    json.dump(data_to_write, file, indent=4)
    print(f"Data written to {file_name}")
# This is a Python script that first writes data to a file and then reads it back, demonstrating file I/O operations.
import json

# Sample data to write to a file
data_to_write = {
    "name": "Alice",
    "age": 20,
    "grade": "A",
    "subjects": ["Math", "Science", "English"],
    "attendance": 95
}

# Specify the file name
file_name = "student_data.json"

# --- Part 1: Write data to the file ---
print(f"Writing data to {file_name}...")
with open(file_name, 'w') as file:
    json.dump(data_to_write, file, indent=4)
print("Data successfully written.")

# --- Part 2: Read data from the file ---
print(f"\nReading data from {file_name}...")
read_data = {} # Initialize an empty dictionary

# Open the file in read mode ('r')
with open(file_name, 'r') as file:
    read_data = json.load(file) # json.load() reads JSON from the file and converts it back to a Python object

print("Data successfully read:")
print(read_data) # Print the Python dictionary that was read
print(f"Type of read_data: {type(read_data)}") # Confirm it's a Python dictionary
    
    