def k_sum(k: int, nums: list[int]) -> int:
    freq = {}  # to store how many times a num occured
    result = 0  # to store the count of pairs
    
    for num in nums:
        complement = k - num   # getting the value need to add to get k
        
        result += freq.get(complement, 0) # adding how many time complement occured
        freq[num] = freq.get(num, 0) + 1  # adding/incersing the num count in freq
    
    return result

print(k_sum(6, [1, 5, 7, -1]))
print(k_sum(6, [1, 5, 7, -1, 5]))