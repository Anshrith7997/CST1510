import random

word_list = ["apple", "banana", "orange", "grape", "mango"]

chosen_word = random.choice(word_list)
placeholder = "_" * len(chosen_word)
guessed_letters = []
lives = 6

print("Welcome to Hangman!")

while lives > 0 and "_" in placeholder:
    print("Word:", placeholder)
    print("Lives:", lives)

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Enter one letter only.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                placeholder = placeholder[:i] + guess + placeholder[i + 1:]
    else:
        lives -= 1

if "_" not in placeholder:
    print("Congratulations! You guessed the word:", chosen_word)
else:
    print("Game over! The word was:", chosen_word)