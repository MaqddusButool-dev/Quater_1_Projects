import random

def play():

    print("****************************************")
    print("   Welcome to Rock, Paper, Scissors!   ")
    print("****************************************")

    user = input("Enter \n R for Rock, \n P for Paper, \n S for Scissors: ").upper()
    computer = random.choice(['R', 'P', 'S'])

    print(f"User: {user}, Computer: {computer}")

    if user == computer:
        print("Match tie!")
    elif user_win(user, computer):
        print("You win!")
    else:
        print("Computer wins! Better luck next time.")

    play_again = input("Do you want to play again? (Y/N): ").upper()
    if play_again == 'Y':
        return play()
    else:
        print("Thanks for playing! Goodbye.")

def user_win(user, computer):
    return (user == 'R' and computer == 'S') or \
           (user == 'P' and computer == 'R') or \
           (user == 'S' and computer == 'P')


print(play())

