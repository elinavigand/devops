# Hangman game
# Author: Elina Vigand
# Disclaimer: Online resources and ChatGPT were used during this project.

word = "troubleshoot"
wrong_guesses = 8
guesses = 0

while guesses < wrong_guesses:
    user_guess = input("Guess a letter: ").lower()
    
    if user_guess in word:
        print("You guessed right!")

    else:
        guesses += 1
        print("Wrong guess!")
        
    if guesses == wrong_guesses:
        print("You have lost the game!")

