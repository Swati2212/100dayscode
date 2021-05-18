from hangman_art import stages, logo
from hangman_words import word_list
import random

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)
word_length = len(chosen_word)
display = []
for _ in range(word_length):
    display += "_"

lives = 6
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

    if guess not in chosen_word:
        print(f"You guessed {guess} that's not in word.You lose a life ")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")

    print(f"{' '.join(display)}")

    if '_' not in display:
        end_of_game = True
        print("You Won!")

    print(stages[lives])
