# Hangman game
# Author: Elina Vigand
# Disclaimer: Online resources and ChatGPT were used during this project.

word = "troubleshoot"
wrong_guesses = 8
guesses = 0
guessed_letters = set()
display_word = ["_" for _ in word]

while guesses < wrong_guesses:
    print("Word: ", display_word)
    user_guess = input("Guess a letter: ").lower()
    
    guessed_letters.add(user_guess)

    # If the guess is right
    if user_guess in word:
        for i, char in enumerate(word):
            if char == user_guess:
                display_word[i] = user_guess
        
        # Check if player has guessed the full word
        if "_" not in display_word:
            print(f"Congratulations! You have guessed the word: {word}")
            break
    
    # If the guess is wrong
    else:
        guesses += 1
        print(f"Wrong guess! You have {wrong_guesses - guesses} guesses left.")

    # Check if the player has reached maximum guesses  
    if guesses == wrong_guesses:
        print(f"You have lost the game! The word was: {word}")

