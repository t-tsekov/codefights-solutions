def arrayPacking(a):
    res = ""
    for i in range(1, len(a) + 1):
        res += "{0:08b}".format(a[-i])

    return int(res, 2)