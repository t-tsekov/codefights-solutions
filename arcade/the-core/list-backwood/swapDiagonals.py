def swapDiagonals(matrix):
    for r in range(len(matrix) // 2):
        matrix[r][r], matrix[r][-1 - r] = matrix[r][-1 - r], matrix[r][r]
        matrix[-1 - r][r], matrix[-1 - r][-1 - r] = matrix[-1 - r][-1 - r], matrix[-1 - r][r]

    return matrix