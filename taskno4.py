import random
def get_user_input():
    user_choice = input("Choose rock (r), paper (p), or scissors (s): ").lower()
    if user_choice not in ['r', 'p', 's']:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return get_user_input()
    return user_choice

def get_computer_choice():
    choices = ['r', 'p', 's']
    return random.choice(choices)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Oops!It's a tie!"
    if user_choice == 'r' and computer_choice == 's':
        return "You win!"
    elif user_choice == 'p' and computer_choice == 'r':
        return "You win!"
    elif user_choice == 's' and computer_choice == 'p':
        return "You win!"
    else:
        return "Better luck next time"


def play_round():
    user_choice = get_user_input()
    computer_choice = get_computer_choice()
    print(f"You chose {user_choice}, the computer chose {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)


def play_game():
    user_score = 0
    computer_score = 0
    while True:
        play_round()
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == 'n':
            print(f"Final Score: You - {user_score}, Computer - {computer_score}")
            break


if __name__ == "__main__":
   play_game()