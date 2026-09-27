"""Calculator exercise — arithmetic operations with input validation."""

def calculator(a: float, b: float, operation: str) -> float:
    if operation == "+":
        return a + b
    if operation == "-":
        return a - b
    if operation == "*":
        return a * b
    if operation == "/":
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    raise ValueError(f"Unknown operation: {operation}")

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter an operator (+, -, *, /): ").strip()
    result = calculator(a, b, op)
    print(f"{a} {op} {b} = {result}")
except ValueError as error:
    print(f"Error: {error}")
