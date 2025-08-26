def Three_Sum(nums: list[int]) -> list[list[int]]:
    nums.sort()     # Sorting the array to use two-pointer technique by adding and subtracting
    result = set()     # to store the triplets uquiqly if we use list we have to check for duplicates in set it automatically checks
    
    for i in range(len(nums) - 2):  # we need 3 numbers to make a triple so len(nums) -3 but range exclude last number so -2
        left, right = i + 1, len(nums) - 1  # assigniging two pointers to ittarate through list
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            # we need to get 0 so if sum < 0 we need to increase the sum by moving left pointer to right
            if current_sum < 0: 
                left += 1
            # samely if sum > 0 we need to decrease the sum by moving right pointer to left
            elif current_sum > 0:
                right -= 1
            # if sum == 0 means it is a triplet save it if not already in set
            else:
                result.add((nums[i], nums[left], nums[right]))
                
                left += 1
                right -= 1  # move both pointers to look for other triplets
    
    return sorted(list(result)) # converting set to list and sorting it for more readbilty


print(Three_Sum([1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 0]))
print(Three_Sum([-1, 0, 1, 2, -1, -4]))
print(Three_Sum([0, 1, 1]))
print(Three_Sum([0, 0, 0])) 