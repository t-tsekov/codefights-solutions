def starRotation(matrix, width, center, t):
    for i in range(t % 8):
        matrix = rotate45(matrix, width, center)
    return matrix


def rotate45(matrix, width, center):
    m = matrix
    r = []
    rad = width // 2
    y, x = center
    for i in range(len(matrix)):
        r.append(matrix[i].copy())

    for i in range(1, rad + 1):

        r[y - i][x] = m[y - i][x - i]
        r[y + i][x] = m[y + i][x + i]

        r[y][x - i] = m[y + i][x - i]
        r[y][x + i] = m[y - i][x + i]

        r[y - i][x + i] = m[y - i][x]
        r[y + i][x - i] = m[y + i][x]

        r[y - i][x - i] = m[y][x - i]
        r[y + i][x + i] = m[y][x + i]

    return r