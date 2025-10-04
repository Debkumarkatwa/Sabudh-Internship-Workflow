def product_except_self(nums):
    n = len(nums)
    answer = [1] * n

    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]
    # print(answer)

    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer


print(product_except_self([1,2,3,4]))
print(product_except_self([-1,1,0,-3,3]))