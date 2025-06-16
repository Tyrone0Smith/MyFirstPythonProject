# greetings.py

# Step 1: Import the 'random' module
# This line brings in the "toolbox" that helps us pick things randomly.
import random

# Step 2: Define a function called 'greet_with_random_message'
# This function will take one piece of information (user_name) as input.
def greet_with_random_message(user_name):
    # Inside the function, we define a list of possible greetings.
    # A list is a collection of items, enclosed in square brackets [].
    greeting_phrases = [
        f"Hello, {user_name}! It's great to see you.",
        f"Hi there, {user_name}! Hope you're having a good day.",
        f"Greetings, {user_name}! How are things going?",
        f"Hey, {user_name}! Welcome back."
    ]

    # Use random.choice() from the 'random' module to pick one phrase from the list.
    chosen_greeting = random.choice(greeting_phrases)

    # Print the chosen greeting.
    print(chosen_greeting)

# --- End of the function definition ---

# Step 3: Get user input
# Ask the user for their name and store it in a variable.
user_input_name = input("What is your name? ")

# Step 4: Call your function
# Now, we "call" or "use" our function, passing the user's name to it.
greet_with_random_message(user_input_name)