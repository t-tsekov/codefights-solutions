def threeSplit(a):
    n = sum(a) / 3

    x = []
    y = []
    t = 0
    for i in range(len(a) - 1):
        t += a[i]
        if t == n:
            x.append(i)
        if t == 2 * n:
            y.append(i)

    c = 0
    for i in x:
        c += sum((j > i) for j in y)

    return c
