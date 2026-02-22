'''
🧠 This script covers:

✅ Basics – Variables, Data Types, Operators, Input/Output
✅ Control Flow – if, for, while, break, continue
✅ Functions – default args, *args, **kwargs, lambda
✅ Data Structures – list, tuple, set, dict
✅ Strings & comprehensions
✅ OOP – class, inheritance, polymorphism, encapsulation
✅ Exception Handling
✅ File Handling
✅ Modules & Packages
✅ Decorators & Generators
✅ Iterators
✅ DateTime & Random
✅ JSON handling
✅ Regex basics
✅ Simple Algorithms (search/sort example
'''

# Full Python All-in-One Example
# =========================================
# PYTHON COMPLETE CONCEPT REVISION SCRIPT
# =========================================

import math
import json
import re
import random
from datetime import datetime

# ---------- BASICS ----------
print("=== BASIC CONCEPTS ===")
x, y = 10, 3
name = "Python"
is_easy = True
print(f"{name} has {len(name)} letters and is_easy = {is_easy}")
print("x + y =", x + y)
print("x ** y =", x ** y)
print("Division:", x / y, "Floor Division:", x // y)

# ---------- INPUT & OUTPUT ----------
# (commented to avoid blocking code)
# user_input = input("Enter your name: ")
# print("Hello", user_input)

# ---------- CONDITIONALS ----------
print("\n=== CONDITIONALS ===")
if x > y:
    print("x is greater than y")
elif x == y:
    print("x equals y")
else:
    print("x is smaller")

# ---------- LOOPS ----------
print("\n=== LOOPS ===")
for i in range(5):
    if i == 2:
        continue
    print("For loop value:", i)

n = 3
while n > 0:
    print("Countdown:", n)
    n -= 1
else:
    print("While loop completed")

# ---------- DATA STRUCTURES ----------
print("\n=== DATA STRUCTURES ===")
lst = [1, 2, 3, 4]
tup = (10, 20, 30)
st = {1, 2, 2, 3}
dic = {"name": "Alice", "age": 25}

lst.append(5)
dic["city"] = "New York"

print("List:", lst)
print("Tuple:", tup)
print("Set:", st)
print("Dictionary:", dic)

# ---------- LIST COMPREHENSION ----------
squares = [i * i for i in range(5)]
print("Squares:", squares)

# ---------- FUNCTIONS ----------
print("\n=== FUNCTIONS ===")
def greet(name="Guest"):
    return f"Hello {name}"

def add_all(*nums):
    return sum(nums)

def describe_person(**info):
    return info

print(greet("Bob"))
print("Sum =", add_all(1, 2, 3, 4))
print("Person info:", describe_person(name="Eve", age=22))

# ---------- LAMBDA ----------
double = lambda a: a * 2
print("Lambda double:", double(5))

# ---------- OOP ----------
print("\n=== OBJECT ORIENTED PROGRAMMING ===")
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

dog = Dog("Buddy")
print(dog.speak())

# ---------- ENCAPSULATION ----------
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private variable

    def deposit(self, amt):
        self.__balance += amt

    def get_balance(self):
        return self.__balance

acc = Account("John", 1000)
acc.deposit(500)
print("Balance:", acc.get_balance())

# ---------- EXCEPTION HANDLING ----------
print("\n=== EXCEPTION HANDLING ===")
try:
    val = 10 / 0
except ZeroDivisionError as e:
    print("Error:", e)
finally:
    print("Finally block always runs")

# ---------- FILE HANDLING ----------
print("\n=== FILE HANDLING ===")
with open("sample.txt", "w") as f:
    f.write("This is a test file.\n")

with open("sample.txt", "r") as f:
    print("File content:", f.read())

# ---------- JSON HANDLING ----------
print("\n=== JSON HANDLING ===")
data = {"name": "Alice", "age": 25}
json_str = json.dumps(data)
print("JSON String:", json_str)
print("Loaded JSON:", json.loads(json_str))

# ---------- DECORATORS ----------
print("\n=== DECORATORS ===")
def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name__} with args {args}")
        return func(*args, **kwargs)
    return wrapper

@debug
def multiply(a, b):
    return a * b

print("Result:", multiply(3, 4))

# ---------- GENERATORS ----------
print("\n=== GENERATORS ===")
def gen_nums(n):
    for i in range(n):
        yield i

for num in gen_nums(5):
    print(num, end=" ")
print()

# ---------- REGEX ----------
print("\n=== REGEX ===")
pattern = r"[A-Za-z]+"
text = "Python3 is fun"
print("Found words:", re.findall(pattern, text))

# ---------- DATETIME & RANDOM ----------
print("\n=== DATETIME & RANDOM ===")
print("Current Time:", datetime.now())
print("Random Choice:", random.choice(["apple", "banana", "cherry"]))

# ---------- ALGORITHMIC EXAMPLE ----------
print("\n=== SIMPLE ALGORITHMS ===")
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [1, 2, 3, 4, 5, 6, 7]
print("Binary search 5 -> index:", binary_search(arr, 5))

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print("Sorted array:", bubble_sort([5, 3, 8, 2, 1]))