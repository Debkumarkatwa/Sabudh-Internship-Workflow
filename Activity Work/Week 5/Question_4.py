def findSingleNumbers(nums):
    xor = 0
    for num in nums:
        xor ^= num

    diff = xor & -xor

    x = 0
    y = 0
    for num in nums:
        if num & diff:
            x ^= num
        else:
            y ^= num
    return [x, y]

print(findSingleNumbers([1, 2, 1, 3, 2, 5]))

print(findSingleNumbers([-1, 0]))

print(findSingleNumbers([0, 1]))