def allLongestStrings(inputArray):
    res = []
    max_len = 0
    for s in inputArray:
        if len(s) > max_len:
            max_len = len(s)
            res = [s]
        elif len(s) == max_len:
            res.append(s)

    return res