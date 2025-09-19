# Custom Exception for negative numbers
class NegativeNumberError(Exception):
    def __init__(self, message="Negative numbers are not allowed"):
        super().__init__(message)


# 1. Take input & printing Division
try:
    num = input("Enter Two numbers (num1, num2): ").split()
except Exception as e:   # Catching any input related error
    print(f"Input Error: {e}")

try:
    if int(num[1]) < 0 or int(num[2]) < 0:
        raise NegativeNumberError("Negative numbers are not allowed.")
    
    result = int(num[1]) / int(num[2])  # May raise ZeroDivisionError/ValueError

except ZeroDivisionError:   # Catching division by zero error
    print("Error: Division by zero is not allowed.")
except NegativeNumberError as e:    # Catching custom exception
    print(f"Error: {e}")
else:   # Executed if no exception occurs
    print(f"Result = {result}")
finally:    # Always executed
    print("Program execution finished.")

'''
If the input is valid and no exceptions occur, the output will be printed.
If there are exceptions, appropriate error messages will be displayed.
if the input is invalid (e.g., non-numeric), an input error message will be shown.

if the input contains negative numbers, the custom NegativeNumberError will be raised and caught.
if There is a number = 0, a ZeroDivisionError will be raised and caught.
'''