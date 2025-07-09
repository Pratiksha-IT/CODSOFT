import random

def get_user_choice():
    choices = {
        "1": "rock",
        "2": "paper",
        "3": "scissors"
    }
    while True:
        print("\nChoose your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        user_input = input("Enter the number of your choice: ")
        if user_input in choices:
            return choices[user_input]
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "win"
    else:
        return "lose"

def display_result(user_choice, computer_choice, result):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if result == "win":
        print("You win this round!")
    elif result == "lose":
        print("You lose this round!")
    else:
        print("It's a tie!")

def play_again_prompt():
    while True:
        print("\nDo you want to play another round?")
        print("1. Yes")
        print("2. No")
        choice = input("Enter the number of your choice: ")
        if choice == "1":
            return True
        elif choice == "2":
            return False
        else:
            print("Invalid input. Please enter 1 or 2.")

def main():
    user_score = 0
    computer_score = 0
    round_number = 0

    print("=" * 30)
    print("  ROCK-PAPER-SCISSORS GAME")
    print("=" * 30)

    while True:
        print("Do you want to play Rock-Paper-Scissors?")
        print("1. Yes")
        print("2. No")
        start_game = input("Enter the number of your choice: ")
        if start_game == "1":
            break
        elif start_game == "2":
            print("Exiting game. Goodbye!")
            return
        else:
            print("Invalid input. Please enter 1 or 2.")

    while True:
        round_number += 1
        print(f"\n--- Round {round_number} ---")

        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        result = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, result)

        if result == "win":
            user_score += 1
        elif result == "lose":
            computer_score += 1

        print(f"Current Score: You {user_score} - Computer {computer_score}")

        if not play_again_prompt():
            break

    print("\n" + "=" * 30)
    print("       GAME OVER")
    print("=" * 30)
    print(f"Final Score: You {user_score} - Computer {computer_score}")
    if user_score > computer_score:
        print("Congratulations! You won the game!")
    elif computer_score > user_score:
        print("Better luck next time! The computer won the game.")
    else:
        print("It's a tie game!")

if __name__ == "__main__":
    main()
