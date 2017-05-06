def rangeBitCount(a, b):
    c = 0
    for i in range(a, b + 1):
        b = "{0:b}".format(i)
        c += b.count("1")

    return c