def extractEachKth(inputArray, k):
    res = []
    for i, x in enumerate(inputArray):
        if (i + 1) % k != 0:
            res.append(x)
    return res