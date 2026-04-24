# Exercise 04 - Loops and Modules

# -----------------------------
# 1. For loop example
# -----------------------------
fruits = ["apple", "banana", "orange", "grape"]

print("Fruits list:")
for fruit in fruits:
    print(fruit)


# -----------------------------
# 2. While loop example
# -----------------------------
print("\nCountdown:")

count = 5
while count > 0:
    print(count)
    count -= 1

print("Done!")


# -----------------------------
# 3. Using a module
# -----------------------------
import math

number = 25
square_root = math.sqrt(number)

print("\nUsing math module:")
print("Square root of", number, "is", square_root)
