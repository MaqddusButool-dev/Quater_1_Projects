
import random 
import hangmanGame.hangman_stages as hangman_stages
import os


def random_word():
    words_List  = ["Hello", "World", "Python", "Programming", "Language", "Computer", "Science", "Engineering", "Software", "Hardware"]
    chosen_word = random.choice(words_List).lower()
    print(chosen_word)
    return chosen_word

def display(word):
    display = []
    for i in range(len(word)):
        display += '_'

    print(display)
    return display

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def hangman():

    
    print("Welcome to Hangman Game!")  
    generated_word = random_word()   
    display_words = display(generated_word)
    attempts = 6
    game_over = False

    while not game_over:
        guessed_letters = input("Enter a letter: ").lower()
        for position in range(len(generated_word)):
            letter = generated_word[position]
            if letter == guessed_letters:
                display_words[position] = letter
        print(display_words)

        if guessed_letters not in generated_word:
            attempts -= 1
            print(f"You have {attempts} attempts left.")
            if attempts == 0:
                game_over = True
                print(f"Game over! The word was: {generated_word}")


        if "_" not in display_words:
            game_over = True
            print(f"Congratulations! You guessed the word: {generated_word}")

        print(hangman_stages.hangman_stages(attempts))
        print("\n")

        

hangman()
        
            
        
