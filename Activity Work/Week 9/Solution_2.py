# Problem 2: Longest Consecutive Sequence

def longestConsecutive(nums: list[int]) -> int:
    """
    Finds the length of the longest consecutive elements sequence in O(n) time.
    Uses a hash set to check for element existence in O(1).
    """
    if not nums:
        return 0
        
    num_set = set(nums)
    max_length = 0
    
    # Iterate through the numbers in the array
    for num in nums:
        # Check if 'num' is the start of a sequence (i.e., 'num - 1' is NOT in the set)
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            
            # Start counting the sequence length
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
                
            max_length = max(max_length, current_length)
            
    return max_length

# --- Test Cases ---
# Example 1
nums1 = [100, 4, 200, 1, 3, 2]
output1 = longestConsecutive(nums1)
print(f"Example 1: Input: {nums1} | Output: {output1}")
# Expected: 4

# Example 2
nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
output2 = longestConsecutive(nums2)
print(f"Example 2: Input: {nums2} | Output: {output2}")
# Expected: 9

# Example 3
nums3 = [1, 0, 1, 2]
output3 = longestConsecutive(nums3)
print(f"Example 3: Input: {nums3} | Output: {output3}")
# Expected: 3