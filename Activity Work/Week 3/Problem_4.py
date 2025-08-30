def trap_water(arr):
    if not arr:
        return 0

    left ,right = 0, len(arr) - 1
    left_max, right_max = 0, 0
    total_water = 0

    while left < right:
        if arr[left] < arr[right]:
            if arr[left] > left_max:
                left_max = arr[left]
            else:
                total_water += left_max - arr[left]
            left += 1
        else:
            if arr[right] > right_max:
                right_max = arr[right]
            else:
                total_water += right_max - arr[right]
            right -= 1
            
    return total_water


print(trap_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

print(trap_water([3, 0, 2, 0, 4]))

print(trap_water([0, 2, 0, 2]))