def Three_Sum(nums: list[int]) -> list:
    nums.sort()     
    result = set()  
    
    for i in range(len(nums) - 2):  
        left, right = i + 1, len(nums) - 1 
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum < 0: 
                left += 1
            
            elif current_sum > 0:
                right -= 1
            
            else:
                result.add((nums[i], nums[left], nums[right]))
                
                left += 1
                right -= 1  
    
    return sorted(list(result)) 


print(Three_Sum([-1,0,1,2,-1,-4]))
print(Three_Sum([0,1,1]))
print(Three_Sum([0, 0, 0])) 