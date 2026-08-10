import random

# List of predefined words
words = ["python", "computer", "programming", "developer", "software"]

# Select a random word
word = random.choice(words)

# Store letters guessed by the player
guessed_letters = []

# Game settings
wrong_guesses = 0
max_wrong_guesses = 6

print("================================")
print("        HANGMAN GAME")
print("================================")

while wrong_guesses < max_wrong_guesses:

    # Display the word with hidden letters
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong guesses:", wrong_guesses)
    print("Remaining chances:", max_wrong_guesses - wrong_guesses)

    # Check whether the player has guessed the complete word
    if "_" not in display_word:
        print("\nCongratulations! You won!")
        print("The word was:", word)
        break

    # Ask the player for a letter
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check repeated guess
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Store the guessed letter
    guessed_letters.append(guess)

    # Check whether the letter exists in the word
    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

else:
    print("\nGame Over!")
    print("You used all 6 incorrect guesses.")
    print("The correct word was:", word)