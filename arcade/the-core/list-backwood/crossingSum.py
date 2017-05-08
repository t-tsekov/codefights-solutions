def crossingSum(matrix, a, b):
    x = matrix[a][b]
    r = sum(matrix[a])
    c = sum([i[b] for i in matrix])
    return c + r - x