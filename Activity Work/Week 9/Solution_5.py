# Problem 5: Find the smallest missing element from a sorted array

def findSmallestMissing(nums: list[int]) -> int:
    """
    Finds the smallest missing non-negative element using binary search.
    Time Complexity: O(log n), Space Complexity: O(1).
    """
    low, high = 0, len(nums) - 1
    
    # Edge case: If the smallest missing element is 0
    if not nums or nums[0] != 0:
        return 0
        
    # Perform binary search
    while low <= high:
        mid = (low + high) // 2
        
        # If the element at index `mid` is equal to `mid`, 
        # the missing element must be in the right half (or after).
        if nums[mid] == mid:
            low = mid + 1
        # If the element at index `mid` is greater than `mid`,
        # the missing element must be in the left half (or is `mid`).
        else:
            high = mid - 1
            
    # After the loop, `low` points to the index of the first element 
    # whose value is greater than its index. This index is the smallest missing number.
    return low

# --- Test Cases ---
# Test case 1
nums1 = [0, 1, 2, 6, 9, 11, 15]
output1 = findSmallestMissing(nums1)
print(f"Test case 1: Input: {nums1} | Output: The smallest missing element is {output1}")
# Expected: 3

# Test case 2
nums2 = [1, 2, 3, 4, 6, 9, 11, 15]
output2 = findSmallestMissing(nums2)
print(f"Test case 2: Input: {nums2} | Output: The smallest missing element is {output2}")
# Expected: 0