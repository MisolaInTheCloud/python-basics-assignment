# Task 1: Variables & Data Types

# String
name = "Misola"
print("Value:", name, "| Type:", type(name))  # Output: Value: Misola | Type: <class 'str'>

# Integer
age = 23
print("Value:", age, "| Type:", type(age))  # Output: Value: 23 | Type: <class 'int'>

# Float
height = 5.7
print("Value:", height, "| Type:", type(height))  # Output: Value: 5.7 | Type: <class 'float'>

# Boolean
is_student = False
print("Value:", is_student, "| Type:", type(is_student))  # Output: Value: False | Type: <class 'bool'>

# List
favorite_colors = ["blue", "green", "red"]
print("Value:", favorite_colors, "| Type:", type(favorite_colors))  # Output: Value: ['blue', 'green', 'red'] | Type: <class 'list'>

# Task 2: User Input & Conditional Statements

# Ask the user to input their age
age_input = input("Enter your age: ")

# Convert input to integer (always needed for numerical comparison)
try:
    age = int(age_input)

    # Conditional check
    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")
except ValueError:
    print("Invalid input. Please enter a numeric value.")

# Task 3: Loops

# For loop: print numbers from 1 to 10
print("For loop: Numbers from 1 to 10")
for i in range(1, 11):
    print(i)

# While loop: print even numbers between 1 and 20
print("While loop: Even numbers between 1 and 20")
num = 2
while num <= 20:
    print(num)
    num += 2

# Task 4: Mini Challenge

# Create a list of 5 fruits
fruits = ["agbalumo", "watermelom", "berry", "mango", "orange"]

# Loop through the list and print each fruit in uppercase
# Skip "watermelon" using continue
print("Fruits in uppercase (excluding 'watermelon'):")
for fruit in fruits:
    if fruit == "watermelon":
        continue  # skip this iteration
    print(fruit.upper())
