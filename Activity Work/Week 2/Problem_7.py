def rotate(matrix: list[list[int]]) -> None:
        n = len(matrix) # number of rows/ columns, since it n x n so both are same

        # Transpose the matrix
        for i in range(n):  # iterating through rows
            for j in range(i, n):   # iterating through columns starting from i to avoid double swapping
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] # swapping the values
        
        '''
        those above steps are transposing the matrix means swapping rows with columns [[1,2], [3,4]] => [[1,3], [2,4]]
        but we need to rotate it 90 degree clockwise so we need to reverse each row to get the final result
        [[1,3], [2,4]] => [[3,1], [4,2]]
        '''
        for row in matrix:  # Reverse each row
            row.reverse()



def rotate2(matrix: list[list[int]]) -> None:
    r = [ 0 * [] for i in range(len(matrix)) ]  # creating empty matrix of same size as input matrix

    for i in range(len(r)):     # iterating through each row
        for j in matrix[::-1]:      # iterating through each column in reverse order
            r[i].append(j[i])       # appending the value to new matrix

    '''
    above steps are creating a new matrix by appending values from input matrix in reverse order of columns
    it is like taking columns from input matrix and making them rows in new matrix in reverse order

    same as solution1 but with extra space. it directly reverses the columns and appends them to new matrix
    '''

    for i in range(len(r)):
        matrix[i] = r[i]    # copying the new matrix to input matrix to make the changes in place

matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix)
print(matrix)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate2(matrix)
print(matrix)


matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
rotate(matrix2)
print(matrix2)

matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
rotate2(matrix2)
print(matrix2)