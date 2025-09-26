class SparseVactor():
    def __init__(self, nums):
        self.nums = nums
        self.non_zero = {i: num for i, num in enumerate(nums) if num != 0}

    def dotProduct(self, vec):
        result = 0
        for i, num in self.non_zero.items():
            if i in vec.non_zero:
                result += num * vec.non_zero[i]
        return result
    
v1 = SparseVactor([1, 0, 0, 2, 3])
v2 = SparseVactor([0, 3, 0, 4, 0])

print(v1.dotProduct(v2))  # Output: 8

v3 = SparseVactor([0, 1, 0, 0, 0])
v4 = SparseVactor([0, 0, 0, 0, 2])

print(v3.dotProduct(v4))  # Output: 0

v5 = SparseVactor([0, 1, 0, 0, 2, 0, 0])
v6 = SparseVactor([1, 0, 0, 0, 3, 0, 4])

print(v5.dotProduct(v6))  # Output: 6