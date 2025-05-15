import random

# Function to get a valid guess from the user
def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please guess a number between 1 and 100.")
        except ValueError:
            print("That's not a valid number. Try again.")

# Function to play the number guessing game
def play_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    print("Welcome to the Number Guessing Game!")
    print(f"You have {max_attempts} attempts to guess the correct number.")
    
    # Start the game loop
    while attempts < max_attempts:
        attempts += 1
        guess = get_user_guess()
        
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
            return True  # Game over, the player won
        
    print(f"Sorry, you've used all your attempts. The correct number was {number_to_guess}.")
    return False  # Game over, the player lost

# Main program execution
def main():
    play_again = "yes"
    
    while play_again.lower() == "yes":
        play_game()
        play_again = input("Do you want to play again? (yes/no): ")
    
    print("Thanks for playing!")

# Call the main function to start the game
if __name__ == "__main__":
    main()
