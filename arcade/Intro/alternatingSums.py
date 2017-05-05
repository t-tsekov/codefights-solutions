def alternatingSums(a):
    first = True
    t1 = 0
    t2 = 0
    for i in range(len(a)):
        if first:
            t1 += a[i]
        else:
            t2 += a[i]
        first = not first

    return [t1, t2]