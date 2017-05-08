def arrayPreviousLess(items):
    res = [0] * len(items)
    for i in range(len(items)):
        changed = False
        for j in range(0, i):
            if items[j] < items[i]:
                res[i] = items[j]
                changed = True
        if not changed:
            res[i] = -1

    return res
