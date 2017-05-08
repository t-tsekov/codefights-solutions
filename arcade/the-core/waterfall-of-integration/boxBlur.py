def boxBlur(image):
    nr = len(image)
    nc = len(image[0])

    res = [[0 for c in range(nc - 2)] for r in range(nr - 2)]

    for r in range(nr - 2):
        for c in range(nc - 2):
            res[r][c] = sum([sum(image[i][c:c + 3]) for i in range(r, r + 3)]) // 9

    return res