def chocolate_distribution(chocolates: list[int], students: int) -> int:
    if students == 0 or len(chocolates) == 0:
        return 0   # checking edge case where no of students or chocolates is 0

    chocolates.sort()   # sorting the chocolates to get the min diff in window
    result = float('inf') # set min_diff to infinity for comparesion

    for i in range(len(chocolates) - students + 1):
        diff = chocolates[i + students - 1] - chocolates[i]
        result = min(result, diff)  # getting the min diff in previous and current window

    return result


print(chocolate_distribution([7, 3, 2, 4, 9, 12, 56], 3))
print(chocolate_distribution([3, 4, 1, 9, 56, 7, 9, 12], 5))