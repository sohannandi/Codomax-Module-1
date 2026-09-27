"""Module 1 — Python basics: Variables, data types, input/output."""

# Strings, integers, floats, booleans, None
name = "Sohan"              # str
age = 21                    # int
gpa = 3.78                  # float
is_active = True            # bool
nothing = None              # NoneType

print(f"Name: {name}")
print(f"Age: {age}")
print(f"GPA: {gpa}")
print(f"Active: {is_active}")
print(f"Nothing value: {nothing}")

# Type conversion examples
age_from_input = int("22")
print(f"Converted age: {age_from_input}, type: {type(age_from_input)}")
