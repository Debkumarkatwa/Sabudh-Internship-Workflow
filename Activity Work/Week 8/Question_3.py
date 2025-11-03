def can_jump(nums: list[int]) -> bool:
    distance = 0
    target = len(nums) - 1
    
    for i, jump in enumerate(nums):
        if i > distance:
            return False
        
        distance = max(distance, i + jump)

        if distance >= target:
            return True
        
    return True  # covers empty or single-element lists

if __name__ == "__main__":
    examples = [
        [2, 3, 1, 1, 4],
        [3, 2, 1, 0, 4],
        [0],
        [2,0,0],
        [1,0,1],
    ]

    for nums in examples:
        result = can_jump(nums)
        print(f"nums = {nums} -> {result}")