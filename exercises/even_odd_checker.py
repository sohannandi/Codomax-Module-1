"""Even/Odd checker — validates user input."""

try:
    number = int(input("Enter an integer: "))
except ValueError:
    print("Invalid input — please enter an integer.")
else:
    print(f"{number} is {'even' if number % 2 == 0 else 'odd'}.")
