import numpy as np
'''
1: Numpy array creation and manipulation 
 
●  Create a 1D Numpy array “a” containing 10 random integers between 0 and 99. 
●  Create a 2D Numpy array “b” of shape (3, 4) containing random integers between -10 and 10. 
●  Reshape “b” into a 1D Numpy array “b_flat”. 
●  Create a copy of “a” called “a_copy”, and set the first element of “a_copy” to -1. 
●  Create a 1D Numpy array “c” containing every second element of “a”. 
'''
a = np.random.randint(0, 100, size=10)  # 1D Numpy array with random integers
    
b = np.random.randint(-10, 11, size=(3, 4)) # 2D Numpy array with shape (3, 4) and random integers
    
b_flat = b.flatten()    # Reshape b into a 1D array
    
a_copy = a.copy()   # copy of a
a_copy[0] = -1
    
c = a[::2]  # 1D array with every second element of a

'''
2: Numpy array indexing and slicing 
 
●  Print the third element of “a”. 
●  Print the last element of “b”. 
●  Print the first two rows and last two columns of “b”. 
●  Assign the second row of “b” to a variable called “b_row”. 
●  Assign the first column of “b” to a variable called “b_col”. 
'''    
print(a[2])  # Third element of a
    
print(b[-1][-1])  # Last element of b
    
print(b[:2, -2:])  # First two rows and last two columns of b
    
b_row = b[1, :]  # Second row of b
    
b_col = b[:, 0]  # First column of b

'''
3: Numpy array operations 
 
●  Create a 1D Numpy array “d” containing the integers from 1 to 10. 
●  Add “a” and “d” element-wise to create a new Numpy array “e”. 
Python Assignment 
●  Multiply “b” by 2 to create a new Numpy array “b_double”. 
●  Calculate the dot product of “b” and “b_double” to create a new Numpy array “f”. 
●  Calculate the mean of “a”,” b”, and “b_double” to create a new Numpy array “g”. 
'''
d = np.arange(1, 11)  # 1D Numpy array with integers from 1 to 10
e = a + d  # Element-wise addition of a and d

b_double = b * 2  # Multiply b by 2

b_double_T = b_double.T  # need transpose for dot
f = np.dot(b, b_double_T)  # Dot product of b and b_double

g = np.array([np.mean(a), np.mean(b), np.mean(b_double)])  # Mean of a, b, and b_double

'''
4: Numpy array aggregation 
 
●  Find the sum of every element in “a” and assign it to a variable “a_sum”. 
●  Find the minimum element in “b” and assign it to a variable “b_min”. 
●  Find the maximum element in “b_double” and assign it to a variable “b_double_max”.
'''

a_sum = np.sum(a)  # Sum of all elements in a
b_min = np.min(b)  # Minimum element in b
b_double_max = np.max(b_double)  # Maximum element in b_double