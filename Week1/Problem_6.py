'''
Write a program to Reverse below given numbers without slicing 
● Test Case 1: 
    Input: 745633 
    Output: 336547 
● Test Case 2: 
    Input: 65346 
    Output: 64356 
'''

number = int(input("Enter a number: "))
reversed_number = 0

while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10

print(reversed_number)
