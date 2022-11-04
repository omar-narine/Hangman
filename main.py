import numbers
import random
import hangman_words
import hangman_art

print(hangman_art.logo)
game_is_finished = False
lives = len(hangman_art.stages) - 1
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
guessed_letters = []

display = []
for _ in range(word_length):
    display += "_"
print(f"{' '.join(display)}\n")

while not game_is_finished:

    guess = input("Guess a letter: ").lower()

    if guess == chosen_word:
        game_is_finished = True
        print(f"Congratulations! You guessed the word '{chosen_word}' correctly!")
    else:

        while guess in guessed_letters or len(guess) > 1 or guess.isdigit():
            if guess in guessed_letters:
                print(f"You've already guessed the letter '{guess}'")
                guess = input("Guess a letter: ").lower()
            elif len(guess) > 1 or guess.isdigit():
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
                print(f"You lose :( \nThe correct word was '{chosen_word}'!")

        if not "_" in display:
            game_is_finished = True
            print(f"Congratulations! You have guessed the word '{chosen_word}' correctly")

        print(hangman_art.stages[lives])
        print("Letters you've guessed: " + f"{', '.join(guessed_letters)}\n")

