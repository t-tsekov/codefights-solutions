def mirrorBits(a):
    return int("{0:b}".format(a)[::-1], 2)
