# This is a number guessing game where the user has to guess a number between 1 and 10.
import random
def guessing_game():
    number_to_guess = random.randint(1, 10)
    attempts = 0
    max_attempts = 3

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 10.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            if guess < 1 or guess > 10:
                print("Please guess a number between 1 and 10.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        attempts += 1

        if guess == number_to_guess:
            print(f"Congratulations! You've guessed the number {number_to_guess} correctly in {attempts} attempts.")
            return
        elif guess < number_to_guess:
            print("Too low!")
        else:
            print("Too high!")

    print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")
if __name__ == "__main__":
    guessing_game()
# This code implements a simple number guessing game.
# The user has three attempts to guess a number between 1 and 10.
# The game provides feedback on whether the guess is too high or too low.
# The game ends when the user guesses correctly or runs out of attempts.    
# The code is structured to handle invalid inputs gracefully.
# The game is initiated by calling the guessing_game function.
# The game can be run by executing the script directly.
# The game uses the random module to select a number.
# The user is prompted to enter their guess, and the game provides feedback.
# The game keeps track of the number of attempts made by the user.
# The game informs the user of the correct number if they fail to guess it.
# The game is designed to be simple and user-friendly.
# The game can be easily modified to change the range of numbers or the number of attempts.
# The game can be extended with additional features, such as difficulty levels or score tracking.
# The game is a fun way to practice basic programming concepts like loops, conditionals, and input handling.
# The game can be used as a learning tool for beginners in programming.
# The game can be played multiple times by running the script again.
# The game can be enhanced with a graphical user interface (GUI) for a better user experience.
# The game can be shared with others to challenge them to guess the number.
# The game can be adapted for different age groups by changing the number range or difficulty.

    
    