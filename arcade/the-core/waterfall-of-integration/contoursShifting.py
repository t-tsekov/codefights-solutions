def contoursShifting(matrix, n_contour = 0):
    ySize, xSize = len(matrix), len(matrix[0])

    if n_contour > (min(xSize, ySize) - 1) // 2:
        return matrix

    indices = get_contour_indices(xSize, ySize, n_contour)

    contour = [matrix[y][x] for x, y in indices]

    # shift contours
    if n_contour % 2 == 0:
        contour = [contour[-1]] + contour[:-1]
    else:
        contour = contour[1:] + [contour[0]]

    # write list back to contour
    for c, (x, y) in zip(contour, indices):
        matrix[y][x] = c

    return contoursShifting(matrix, n_contour + 1)


def get_contour_indices(xSize, ySize, nContour):
    width = (xSize - 2 * nContour)
    height = (ySize - 2 * nContour)

    indX = list(range(nContour, xSize - nContour))
    indX += [xSize - nContour - 1] * (height - 1)

    indY = [nContour] * width
    indY += range(nContour + 1, ySize - nContour)

    if min(xSize, ySize) != nContour * 2 + 1:
        indX += range(xSize - nContour - 2, nContour - 1, -1)
        indX += [nContour] * (height - 2)

        indY += [ySize - nContour - 1] * (width - 1)
        indY += range(ySize - nContour - 2, nContour, -1)

    return list(zip(indX, indY))