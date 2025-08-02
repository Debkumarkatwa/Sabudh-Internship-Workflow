'''
Write a Python program to find the median of three values. 
● Test case 1: 
  Input:  
    Input first number: 15 
    Input second number: 26 
    Input third number: 29 
    Output : 26 
● Test case 2: 
  Input:  
    Input first number: 10 
    Input second number: 20 
    Input third number: 5  
    Output : 10 
'''

first_number = int(input("Input first number: "))
second_number = int(input("Input second number: "))
third_number = int(input("Input third number: "))

numbers = [first_number, second_number, third_number]
numbers.sort()

print(numbers[1])
