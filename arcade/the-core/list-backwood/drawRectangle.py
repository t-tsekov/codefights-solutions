def drawRectangle(canvas, rectangle):
    x1, y1, x2, y2 = rectangle

    canvas[y1][x1:x2 + 1] = '*' + '-' * (x2 - x1 - 1) + '*'
    canvas[y2][x1:x2 + 1] = '*' + '-' * (x2 - x1 - 1) + '*'

    for y in range(y1 + 1, y2):
        canvas[y][x1] = '|'
        canvas[y][x2] = '|'

    return canvas