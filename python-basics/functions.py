"""Module 1 — Python basics: Functions."""

def greet(name: str = "friend") -> str:
    return f"Hello, {name}!"

def add(a: float, b: float) -> float:
    return a + b

def calculate_bmi(weight_kg: float, height_m: float) -> float:
    if height_m <= 0:
        raise ValueError("Height must be positive.")
    return weight_kg / (height_m ** 2)

# Usage
print(greet())
print(greet("Sohan"))
print(add(3, 4))
print(f"BMI: {calculate_bmi(70, 1.75):.2f}")
