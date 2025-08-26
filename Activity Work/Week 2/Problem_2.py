def arrange_array(nums: list[int]) -> list[int]:
    positive = -1    # alocating positive number index (for now -1)

    for index in range(len(nums)):
        if nums[index] >= 0 and positive == -1: # checking for 1st positive number index
            positive = index        # assing the positive index

        if nums[index] < 0 and positive != -1:  # after finding positive num if negative num found 
            nums.insert(positive, nums[index])  # insert negative num at positive index
            # as this step increse the len of the list we push all values by 1 position right
            # so we need to remove the duplicate negative number which is at index + 1

            nums.pop(index + 1)

            positive += 1 # incresing positive index for next value

    return nums
                        
print(arrange_array([-12, 11, -13, -5, 6, -7, 5, -3, -6])) 
print(arrange_array([-12, 11, 13, -5, 6, -7, 5, -3, 8]))
print(arrange_array([0, -9, 12, 11, 13, 5, 6, -50, 5, 3, 8, -1, -2, -3, -4, -5, -6]))