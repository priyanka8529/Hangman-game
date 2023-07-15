import random

# Function to update the displayed word with guessed letters
def update_guessed_word():
    guessed_word = ""
    for letter in word_to_guess:
        if letter in guessed_letters:
            guessed_word += letter + " "
        else:
            guessed_word += "_ "
    print(guessed_word)

# Function to check if the guessed letter is correct
def check_guess(guessed_letter):
    if guessed_letter.isalpha() and len(guessed_letter) == 1:
        guessed_letters.append(guessed_letter.lower())
        update_guessed_word()

        if set(word_to_guess) == set(guessed_letters):
            print("Congratulations! You won!")
            reset_game()

        elif guessed_letter.lower() not in word_to_guess:
            wrong_guesses.append(guessed_letter)
            update_hangman_image()

# Function to update the hangman image for wrong guesses
def update_hangman_image():
    print("Wrong guesses:", ", ".join(wrong_guesses))
    print(hangman_images[len(wrong_guesses)])
    if len(wrong_guesses) == len(hangman_images) - 1:
        print("Game Over! You lost! The word was:", word_to_guess)
        reset_game()

# Function to reset the game
def reset_game():
    global word_to_guess, guessed_letters, wrong_guesses
    word_to_guess = random.choice(word_list)
    guessed_letters = []
    wrong_guesses = []
    update_guessed_word()

# List of words for the game
word_list = ["hangman", "python", "game", "play", "openai"]

# Hangman images
hangman_images = [
    """
    +---+
    |   |
        |
        |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\\  |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\\  |
   /    |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
    =========
    """
]

# Initialize game variables
word_to_guess = random.choice(word_list)
guessed_letters = []
wrong_guesses = []

# Start the game
update_guessed_word()

# Game loop
while True:
    guessed_letter = input("Enter a letter: ")
    check_guess(guessed_letter)
