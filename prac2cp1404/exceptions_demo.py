"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? when the input for the denominator and numerator is the right type but wrong value
2. When will a ZeroDivisionError occur? when we put the denominator 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
denominator = int(input("Enter the denominator"))
    while denominator == 0:
        print("denominator can not be 0")
        denominator = int(input("Enter the denominator"))
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
