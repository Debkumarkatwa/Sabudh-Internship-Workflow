'''
Read an integer N. For all non-negative integers i < N, print i^2.  
● Test Case 1 
    Input: 5 
    Output :  [0, 1, 4, 9, 16] 
● Test Case 2 
    Input: 4 
    Output: [0, 1, 4, 9]
'''

n = int(input("Enter an integer N: "))
result = [i**2 for i in range(n)]
print(result)