def Target_in_Matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Start from the top-right corner of the matrix
    row, col = 0, cols - 1
    
    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return True
        
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1
            
    return False


# Example usage
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
print(Target_in_Matrix(matrix, 5))

print(Target_in_Matrix(matrix, 20))