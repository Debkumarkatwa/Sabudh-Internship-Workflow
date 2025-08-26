'''
Write a Python function to calculate the factorial of a number (a non-negative integer).
The function accepts the number as an argument. 
● Test case 1: 
    Input = 4 
    output = 24 
● Test case 2: 
    Input = 2 
    output = 2 
'''
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
    

n = int(input("Enter a non-negative integer: "))
result = factorial(n)
print(result)