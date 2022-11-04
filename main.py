import random
import hangman_words
import hangman_art

print(hangman_art.logo)
game_is_finished = False
lives = len(hangman_art.stages) - 1
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
guessed_letters = []

# Testing code
print(f"The word to guess is: {chosen_word}")

display = []
for _ in range(word_length):
    display += "_"

while not game_is_finished:

    guess = input("Guess a letter: ").lower()

    while guess in guessed_letters or len(guess) > 1:
        if guess in guessed_letters:
            print(f"You've already guessed the letter '{guess}'")
            guess = input("Guess a letter: ").lower()
        elif len(guess) > 1:
            print(f"'{guess}' is not a valid input. Please only enter single letters")
            guess = input("Guess a letter: ").lower()

    guessed_letters.append(guess)

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("You lose.")

    if not "_" in display:
        game_is_finished = True
        print("You win.")

    print(hangman_art.stages[lives])

    print("Letters you've guessed: " + f"{', '.join(guessed_letters)}")
