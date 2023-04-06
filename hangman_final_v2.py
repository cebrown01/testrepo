import hangman_art
import hangman_words
import random
import os

def clear():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

play_again = True

while play_again:
    chosen_word = random.choice(hangman_words.word_list)
    display = []
    guessed_letters = ""
    lives = 6
    done = False

    for letter in chosen_word:
        display += "_"

    clear()

    while not done:
        #print(f"You random word is {chosen_word}")
        print(hangman_art.logo)
        print(hangman_art.stages[lives])
        print(" ".join(display))
        print(f"Letters previously guessed: {guessed_letters}")
        guess = input("\nGuess a letter: ").lower()
        if len(guess) > 1:
            clear()
            print("!!!Invalid input, please enter only one letter at a time!!!")
        else:
            if guess in guessed_letters:
                print(f"You've already guessed the letter {guess}")
            else:
                guessed_letters += guess + " "
                for position in range(len(chosen_word)):
                    if guess == chosen_word[position]:
                        display[position] = guess
                
                if guess not in chosen_word:
                    lives -= 1

            if "_" not in display:
                print(" ".join(display))
                print("You Win!")
                done = True
            else:
                clear()

            if lives == 0:
                print(hangman_art.logo)
                print(hangman_art.stages[lives])
                print("You lose!")
                done = True
    again = input("Play again? (y or n): ").lower()
    if again == "n":
        play_again = False


    