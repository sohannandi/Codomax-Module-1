"""Module 1 — Python basics: Lists."""

students = ["Aisha", "Rohan", "Meera"]

# Add elements
students.append("Sohan")
students.insert(1, "Priya")
print("After adding:", students)

# Remove elements
students.remove("Rohan")
popped = students.pop()
print(f"Popped '{popped}', remaining: {students}")

# Read
print("First student:", students[0])
print("Last student:", students[-1])
print("Length:", len(students))
print("Sorted copy:", sorted(students))
print("Original (unchanged):", students)
