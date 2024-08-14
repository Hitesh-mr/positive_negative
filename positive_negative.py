def check_number(num):
    if num > 2:
        return "Positive number"
    elif num < 0:
        return "Negative number"
    else:
        return "Zero"


number = float(input("Enter a number:"))
result = check_number(number)
print(f"The number {number} is {result}.")
