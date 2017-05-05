def matrixElementsSum(matrix):
    sum = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if row > 0:
                if matrix[row -1][col] == 0:
                    matrix[row][col] = 0
            sum += matrix[row][col]
    return sum