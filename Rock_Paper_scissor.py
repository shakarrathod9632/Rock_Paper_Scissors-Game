import random  # Import the random module to generate random choices

# Initialize scores to keep track of the game progress
user_score = 0
computer_score = 0

# Function to get the user's choice
def get_user_choice():
    # Prompt the user to enter a choice among rock, paper, or scissors
    choice = input("Enter a choice (rock, paper, scissors): ")
    # Validate the user's input and repeat the prompt if the input is invalid
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid input.")
        choice = input("Enter a choice (rock, paper, scissors): ")
    # Return the valid input
    return choice

# Function to get the computer's choice
def get_computer_choice():
    # Randomly select and return one of the options: rock, paper, or scissors
    return random.choice(["rock", "paper", "scissors"])

# Function to determine the winner of the game
def determine_winner(user_choice, computer_choice):
    # Access the global score variables to update them
    global user_score, computer_score
    # Check if both choices are the same, resulting in a tie
    if user_choice == computer_choice:
        return "It's a tie!"
    # Check all winning conditions for the user
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        user_score += 1  # Increment user's score
        return "You win!"
    # If it's not a tie and the user hasn't won, then the computer wins
    else:
        computer_score += 1  # Increment computer's score
        return "You lose!"

# Function to print the current score
def print_score():
    # Print the current score of the user and the computer
    print(f"Your score: {user_score} | Computer score: {computer_score}")

# Main function to play the game
def play_game():
    # Access the global score variables
    global user_score, computer_score
    # Start an infinite loop to play the game continuously
    while True:
        # Get the choices of the user and the computer
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        # Print out the choices to inform the players
        print(f"\nYou chose {user_choice}, computer chose {computer_choice}.")
        # Determine the winner and print the result
        print(determine_winner(user_choice, computer_choice))
        # Print the updated score after each round
        print_score()

        # Ask the user if they want to play again
        play_again = input("Play again? (yes/no): ")
        # Break the loop if the user doesn't want to continue
        if play_again.lower() != "yes":
            break

# Check if the script is run directly (not imported)
if __name__ == "__main__":
    # If the script is run directly, start the game
    play_game()
