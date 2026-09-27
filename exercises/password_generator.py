"""Password generator — uses loops, lists, and random."""

import random

letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = list("!@#$%^&*")

try:
    length = int(input("How many characters? "))
except ValueError:
    print("Invalid length — please enter an integer.")
else:
    if length <= 0:
        print("Length must be positive.")
    else:
        chars = letters + numbers + symbols
        password = [random.choice(chars) for _ in range(length)]
        random.shuffle(password)
        print(f"Generated password: {''.join(password)}")
