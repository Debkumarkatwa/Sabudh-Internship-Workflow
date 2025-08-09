# 1. Write a Python program to multiply all the items in a list.
def List_Multiply(List:list) -> int:
    if not List:
        return 0
    
    product = 1
    for number in List:
        product *= number
    return product

# 2. Write a Python program to get the largest number from a list."
def List_Largest(List:list) -> int:
    if not List:
        return None

    # return max(List)

    largest = List[0]
    for number in List:
        if number > largest:
            largest = number
    return largest

# 3. Write a Python program to get the smallest number from a list."
def List_Smallest(List:list) -> int:
    if not List:
        return None

    # return min(List)

    smallest = List[0]
    for number in List:
        if number < smallest:
            smallest = number
    return smallest

# 4. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
def Tupple_Sort(List:list) -> list:
    if not List:
        return []

    sorted_list = sorted(List, key=lambda x: x[-1])
    return sorted_list

# 5. Write a Python program to remove duplicates from a list.
def Remove_Duplicates(List:list) -> list:
    if not List:
        return []

    # return list(set(List))

    unique_list = []
    for item in List:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# 6. Write a Python program to check if a list is empty or not.
def Is_Empty(List:list) -> bool:
    return len(List) == 0

# 7. write a python program to count the lowercase letters in a given list of word 
def Count_Lowercase(List:list) -> list:
    if not List:
        return 0

    count = 0
    result = []
    for word in List:
        for char in word:
            if char.islower():
                count += 1
        result.append(count)
        count = 0
    return result

'''
9. Write a Python program to extract all elements from a given list that appear a specified number of times consecutively (i.e., one after another, without interruption).
Examples:
    ○ Input list: [1, 1, 3, 4, 4, 5, 6, 7]
    Number of consecutive elements to extract: 2
    ○ Output: [1, 4]
    (Because 1 appears twice in a row, and 4 also appears twice in a row)
    ○ Input list: [0, 1, 2, 3, 4, 4, 4, 4, 5, 7]
    Number of consecutive elements to extract: 4
    ○ Output: [4]
    (Because only 4 appears four times in a row)
'''
def Extract_Consecutive(List:list, n:int) -> list:
    if not List or n <= 0:
        return []

    result = []
    count = 1

    for i in range(1, len(List)):
        if List[i] == List[i - 1]:
            count += 1
        else:
            if count == n:
                result.append(List[i - 1])
            count = 1

    if count == n:   # Checking the last one
        result.append(List[-1])

    return result

'''
10. Write a Python program to find the largest odd number in a given list of integers.
If there are no odd numbers in the list, the program should indicate that as well.
Examples:
    ○ Input: [0, 9, 2, 4, 5, 6] → Output: 9
    ○ Input: [-4, 0, 6, 1, 0, 2] → Output: 1
    ○ Input: [1, 2, 3] → Output: 3
    ○ Input: [-4, 0, 5, 1, 0, 1] → Output: 5
    ○ Input: [2, 4, 6] → Output: "No odd numbers found"
'''
def Largest_Odd(List:list) -> int:
    if not List:
        return "No odd numbers found"

    largest_odd = None

    for number in List:
        if number % 2 != 0 and (largest_odd is None or number > largest_odd):
            largest_odd = number

    return largest_odd if largest_odd is not None else "No odd numbers found"

'''
11. Write a Python program to remove specific elements (at the 0th, 4th, and 5th positions) from a given list and print the resulting list.
    ○ Sample List : [A, B, C, D, E, F]
    ○ Expected Output : [B, C, D]
'''
def Remove_Specific_Elements(List:list) -> list:
    if not List:
        return []

    indices_to_remove = {0, 4, 5}
    result = []
    for i in range(len(List)):
        if i not in indices_to_remove:
            result.append(List[i])
            
    return result

# Test Cases for List_Multiply
print("Testing List_Multiply:")
print(f"List_Multiply([1, 2, 3, 4, 5]): {List_Multiply([1, 2, 3, 4, 5])}")
print(f"List_Multiply([]): {List_Multiply([])}")
print(f"List_Multiply([2, -3, 4]): {List_Multiply([2, -3, 4])}")
print("-" * 20, '\n')

# Test Cases for List_Largest
print("Testing List_Largest:")
print(f"List_Largest([1, 5, 2, 8, 3]): {List_Largest([1, 5, 2, 8, 3])}")
print(f"List_Largest([]): {List_Largest([])}")
print(f"List_Largest([-1, -5, -2]): {List_Largest([-1, -5, -2])}")
print("-" * 20, '\n')

# Test Cases for List_Smallest
print("Testing List_Smallest:")
print(f"List_Smallest([1, 5, 2, 8, 3]): {List_Smallest([1, 5, 2, 8, 3])}")
print(f"List_Smallest([]): {List_Smallest([])}")
print(f"List_Smallest([-1, -5, -2]): {List_Smallest([-1, -5, -2])}")
print("-" * 20, '\n')

# Test Cases for List_Sort
print("Testing Tupple_Sort:")
print(f"Tupple_Sort([(1, 2), (3, 1), (2, 4)]): {Tupple_Sort([(1, 2), (3, 1), (2, 4)])}")
print(f"Tupple_Sort([]): {Tupple_Sort([])}")
print(f"Tupple_Sort([(1, 2., -5), (1, 2)]): {Tupple_Sort([(1, 2, -5), (1, 2)])}")
print("-" * 20, '\n')

# Test Cases for Remove_Duplicates
print("Testing Remove_Duplicates:")
print(f"Remove_Duplicates([1, 2, 2, 3, 1, 4]): {Remove_Duplicates([1, 2, 2, 3, 1, 4])}")
print(f"Remove_Duplicates([]): {Remove_Duplicates([])}")
print(f"Remove_Duplicates([5,0,0,0,0]): {Remove_Duplicates([5,0,0,0,0])}")
print("-" * 20, '\n')

# Test Cases for Is_Empty
print("Testing Is_Empty:")
print(f"Is_Empty([1, 2, 3]): {Is_Empty([1, 2, 3])}")
print(f"Is_Empty([]): {Is_Empty([])}")
print("-" * 20, '\n')

# Test Cases for Count_Lowercase
print("Testing Count_Lowercase:")
print(f"Count_Lowercase(['Hello', 'World', 'Test']): {Count_Lowercase(['Hello', 'World', 'Test'])}")
print(f"Count_Lowercase([]): {Count_Lowercase([])}")
print(f"Count_Lowercase(['UPPER', 'CASE']): {Count_Lowercase(['UPPER', 'CASE'])}")
print(f"Count_Lowercase(['a', 'b', 'c']): {Count_Lowercase(['a', 'b', 'c'])}")
print("-" * 20, '\n')

# Test Cases for Extract_Consecutive
print("Testing Extract_Consecutive:")
print(f"Extract_Consecutive([1, 1, 2, 3, 3, 3, 4, 4], 2): {Extract_Consecutive([1, 1, 2, 3, 3, 3, 4, 4], 2)}")
print(f"Extract_Consecutive([], 2): {Extract_Consecutive([], 2)}")
print(f"Extract_Consecutive([1, 1, 1, 1], 3): {Extract_Consecutive([1, 1, 1, 1], 3)}")
print(f"Extract_Consecutive([1, 2, 3, 4], 1): {Extract_Consecutive([1, 2, 3, 4], 1)}")
print(f"Extract_Consecutive([1, 1, 1, 2, 2, 2], 2): {Extract_Consecutive([1, 1, 1, 2, 2, 2], 2)}")
print("-" * 20, '\n')

# Test Cases for Largest_Odd
print("Testing Largest_Odd:")
print(f"Largest_Odd([1, 2, 3, 4, 5]): {Largest_Odd([1, 2, 3, 4, 5])}")
print(f"Largest_Odd([]): {Largest_Odd([])}")
print(f"Largest_Odd([-1, -3, -5]): {Largest_Odd([-1, -3, -5])}")
print("-" * 20, '\n')

# Test Cases for Remove_Specific_Elements
print("Testing Remove_Specific_Elements:")
print(f"Remove_Specific_Elements([10, 20, 30, 40, 50, 60, 70]): {Remove_Specific_Elements([10, 20, 30, 40, 50, 60, 70])}")
print(f"Remove_Specific_Elements([]): {Remove_Specific_Elements([])}")
print(f"Remove_Specific_Elements([100]): {Remove_Specific_Elements([100])}")
print("-" * 20, '\n')