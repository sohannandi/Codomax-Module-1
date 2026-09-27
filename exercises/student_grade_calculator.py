"""Student grade calculator — uses conditionals."""

try:
    score = float(input("Enter student score (0-100): "))
except ValueError:
    print("Invalid input — please enter a number.")
else:
    if 0 <= score <= 100:
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
        print(f"Score: {score} | Grade: {grade}")
    else:
        print("Score must be between 0 and 100.")
