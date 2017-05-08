dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def cellPerimeter(cell, matrix):
    count = 4
    for dx, dy in dirs:
        x = cell[0] + dx
        y = cell[1] + dy
        if 0 <= x < len(matrix[0]) and 0 <= y < len(matrix) and matrix[y][x]:
            count -= 1
    return count


def polygonPerimeter(matrix):
    count = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x]:
                count += cellPerimeter((x, y), matrix)
    return count
