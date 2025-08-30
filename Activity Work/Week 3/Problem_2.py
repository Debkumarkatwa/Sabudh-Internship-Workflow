def max_product(arr: list[int]) -> tuple[int, int, int] | None:
    if len(arr) < 3:    # To handle edge case
        return None

    arr.sort()
    # Two possibilities:
    # 1. Product of three largest numbers
    prod1 = arr[-1] * arr[-2] * arr[-3]
    triplet1 = (arr[-3], arr[-2], arr[-1])
    
    # 2. Product of two smallest (possibly negative) and the largest
    prod2 = arr[0] * arr[1] * arr[-1]
    triplet2 = (arr[0], arr[1], arr[-1])

    if prod1 > prod2:
        return triplet1
    else:
        return triplet2

# Example usage
arr = [-4, 1, -8, 9, 6]
print(f"The triplet having the maximum product is {max_product(arr)}")
arr2 = [1, 7, 2, -2, 5]
print(f"The triplet having the maximum product is {max_product(arr2)}")