#Exercise4.10 Guess the Number & Modification

import random

def play_game():
    secret_number = random.randint(1, 1000)
    guess_count = 0
    print("Guess my number between 1 and 1000 with the fewest guesses:")

    while True:
        guess = int(input("Enter your guess: "))
        guess_count += 1

        if guess < secret_number:
            print("Too low. Try again.")
        elif guess > secret_number:
            print("Too high. Try again.")
        else:
            print("Congratulations. You guessed the number!")
