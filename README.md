# 🔢 Number Checker in Python

This is a beginner-friendly Python project that checks whether a given number is **positive**, **negative**, or **zero**.  
It demonstrates the use of conditional statements (`if`, `elif`, `else`) in Python.

---

## 🚀 Features
- Takes user input (number).
- Checks if the number is:
  - Positive
  - Negative
  - Zero
- Prints the result in a user-friendly format.

---

## 🧑‍💻 Code Example

```python
def check_number(num):
    if num > 0:
        return "Positive number"
    elif num < 0:
        return "Negative number"
    else:
        return "Zero"

number = float(input("Enter a number: "))
result = check_number(number)
print(f"The number {number} is {result}.")
