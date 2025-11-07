# Problem 3: Longest Increasing Subsequence

import bisect

def lengthOfLIS(nums: list[int]) -> int:
    """
    Finds the length of the LIS using a patience sorting approach (O(n log n)).
    'tails' stores the smallest tail of all increasing subsequences of length i+1.
    """
    tails = [] 
    
    # Iterate through each number in the input array
    for num in nums:
        # Find the smallest tail that is >= num using binary search
        # bisect_left returns an index 'i' such that all tails[:i] < num
        # and all tails[i:] >= num.
        i = bisect.bisect_left(tails, num)
        
        # If num is greater than all tails, it extends the longest sequence by 1
        if i == len(tails):
            tails.append(num)
        # Otherwise, replace the tail of the sequence of length i+1 
        # with a smaller value (num) to allow for potentially longer subsequences later.
        else:
            tails[i] = num
            
    # The length of 'tails' is the length of the LIS
    return len(tails)

# --- Test Cases ---
# Example 1
nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
output1 = lengthOfLIS(nums1)
print(f"Example 1: Input: {nums1} | Output: {output1}")
# Expected: 4

# Example 2
nums2 = [0, 1, 0, 3, 2, 3]
output2 = lengthOfLIS(nums2)
print(f"Example 2: Input: {nums2} | Output: {output2}")
# Expected: 4

# Example 3
nums3 = [7, 7, 7, 7, 7, 7, 7, 7]
output3 = lengthOfLIS(nums3)
print(f"Example 3: Input: {nums3} | Output: {output3}")
# Expected: 1