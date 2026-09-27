"""Number guessing game — uses loops, conditionals, and random."""

import random

secret = random.randint(1, 100)
attempts = 0
print("I'm thinking of a number between 1 and 100. Guess it!")

while True:
    try:
        guess = int(input("Your guess: "))
        attempts += 1
        if guess < secret:
            print("Too low — try again.")
        elif guess > secret:
            print("Too high — try again.")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break
    except ValueError:
        print("Please enter a valid integer.")
