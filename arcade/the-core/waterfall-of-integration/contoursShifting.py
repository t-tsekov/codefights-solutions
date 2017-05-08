ef
contoursShifting(matrix):
s = [row[:] for row in matrix]
n = len(matrix)
m = len(matrix[0])
for i in range(n / 2 + 1):
    t = rot([row[i:m - i] for row in matrix[i:n - i]], i % 2)
    for x in range(i, n - i):
        for y in range(i, m - i):
            s[x][y] = t[x - i][y - i]
return s


def rot(m, c):
    if len(m) == 0:
        return m
    if len(m[0]) == 0:
        return m
    r = [row[:] for row in m]
    if c == 0:
        for j in range(1, len(m[0])):
            r[0][j] = m[0][j - 1]
        for i in range(1, len(m)):
            r[i][-1] = m[i - 1][-1]
        if len(m) == 1:
            r[0][0] = m[0][-1]
            return r
        if len(m[0]) == 1:
            r[0][0] = m[-1][0]
            return r
        for j in range(0, len(m[0]) - 1):
            r[-1][j] = m[-1][j + 1]
        for i in range(0, len(m) - 1):
            r[i][0] = m[i + 1][0]
    if c == 1:
        for j in range(0, len(m[0]) - 1):
            r[0][j] = m[0][j + 1]
        for i in range(0, len(m) - 1):
            r[i][-1] = m[i + 1][-1]
        if len(m) == 1:
            r[0][-1] = m[0][0]
            return r
        if len(m[0]) == 1:
            r[-1][0] = m[0][0]
            return r
        for j in range(1, len(m[0])):
            r[-1][j] = m[-1][j - 1]
        for i in range(1, len(m)):
            r[i][0] = m[i - 1][0]
    return r