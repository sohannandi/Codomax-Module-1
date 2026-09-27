"""Module 1 — Python basics: Loops."""

# for loop example
print("Counting to 5:")
for i in range(1, 6):
    print(f"  {i}")

# List traversal
colors = ["red", "green", "blue"]
print("Colors:")
for color in colors:
    print(f"  - {color}")

# while loop with break/continue
print("Odd numbers 1-9:")
n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue
    print(f"  {n}")
