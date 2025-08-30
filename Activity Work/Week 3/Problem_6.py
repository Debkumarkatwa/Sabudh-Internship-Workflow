def spiralOrder(matrix):
    if not matrix or not matrix[0]:     # Handling empty matrix case
        return []
    
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Traverse from left to right
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        # Traverse downwards
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        # Traverse from right to left
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        # Traverse upwards
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1
            

    return result

# Example usage:
matrix = [
    [1, 2, 3,4],
    [5, 6,7, 8],
    [9,10,11,12]
]
print(spiralOrder(matrix))  # Output: [1,2,3,6,9,8,7,4,5]