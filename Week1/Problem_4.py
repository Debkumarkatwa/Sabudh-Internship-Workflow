'''
Write a program to count the total number of digits in a number using a while loop 
● Test Case 1: 
    Input: 75869 
    Output: 5 
● Test Case 2: 
    Input: 654 
    Output: 3 
'''

def count_digits(number):
    count = 0

    while number > 0:
        number //= 10
        count += 1

    return count


number = int(input("Enter a number: "))
count = 0

while number > 0:
    number //= 10
    count += 1

print(count)