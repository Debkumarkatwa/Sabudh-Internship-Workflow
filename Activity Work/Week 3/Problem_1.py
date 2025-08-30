def subarraySum(arr: list[int], k: int) -> int:
    max_len = 0
    feq = {0:[-1]}

    tempsum = 0
    for i in arr:
        tempsum += i
        
        if tempsum - k in feq:
            for j in feq[tempsum - k]:
                max_len = max(max_len, i - j)

        if tempsum in feq:
            feq[tempsum].append(i)
        else:
            feq[tempsum] = [i]

    return max_len 


print(subarraySum(arr = [10, 5, 2, 7, 1, -10], k = 15))
print(subarraySum(arr = [-5, 8, -14, 2, 4, 12], k = -5))
print(subarraySum(arr = [10, -10, 20, 30], k = 5))
