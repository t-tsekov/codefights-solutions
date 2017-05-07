def differentSquares(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    twoByTwos = []
    if rows >= 2 and columns >= 2:
        for x in range(columns-1):
            for y in range(rows-1):
                twoByTwos.append((matrix[y][x],matrix[y][x+1],matrix[y+1][x],matrix[y+1][x+1]))
    else:
        count = 0
    return len(set(twoByTwos))