import random

words = ["python", "laptop", "program", "engineer", "network"]

word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("===== Welcome to Hangman Game =====")

while wrong_guesses < max_wrong:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        wrong_guesses += 1
        print("Wrong Guess!")
        print(f"Remaining Chances: {max_wrong - wrong_guesses}")

else:
    print("\nGame Over!")
    print("The word was:", word)