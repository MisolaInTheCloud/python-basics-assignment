# python-basics-assignment
# Task 1: Variables & Data Types

# String
name = "Alice"
print("Value:", name, "| Type:", type(name))  # Output: Value: Alice | Type: <class 'str'>

# Integer
age = 30
print("Value:", age, "| Type:", type(age))  # Output: Value: 30 | Type: <class 'int'>

# Float
height = 5.7
print("Value:", height, "| Type:", type(height))  # Output: Value: 5.7 | Type: <class 'float'>

# Boolean
is_student = False
print("Value:", is_student, "| Type:", type(is_student))  # Output: Value: False | Type: <class 'bool'>

# List
favorite_colors = ["blue", "green", "red"]
print("Value:", favorite_colors, "| Type:", type(favorite_colors))  # Output: Value: ['blue', 'green', 'red'] | Type: <class 'list'>

# Task 2: Decision Making with if-elif-else

user_age = int(input("Enter your age: "))

if user_age < 13:
    print("You are a child.")
elif user_age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")

# Task 3: Looping with for

fruits = ["apple", "banana", "mango", "grape", "pineapple"]

for fruit in fruits:
    print(fruit.upper())

# Task 4: Looping with while

num = 1
while num <= 5:
    print("Current number:", num)
    num += 1
