def maxSubArray(nums: list[int]) -> int:
    current_sum = 0
    max_sum = nums[0]

    for index in range(len(nums)):
        current_sum += nums[index]

        if current_sum > max_sum:
            max_sum = current_sum

        if current_sum < 0:
            current_sum = 0

    return max_sum    
    

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
print(maxSubArray([1]))  # Output: 1