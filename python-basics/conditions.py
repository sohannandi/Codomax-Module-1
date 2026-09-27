"""Module 1 — Python basics: Conditional statements."""

# Even / odd checker (accepts user input with validation)
try:
    number = int(input("Enter an integer: "))
except ValueError:
    print("Invalid input — please enter an integer.")
else:
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

# Simple grade calculator
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Score {score} → Grade {grade}")
