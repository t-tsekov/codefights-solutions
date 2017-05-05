def allLongestStrings(inputArray):
    res = []
    max_len = max([len(x) for x in inputArray])
    for i in inputArray:
        if len(i) == max_len:
            res.append(i)
    return res

