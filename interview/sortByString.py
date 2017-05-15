def sortByString(s, t):
    d = {}
    res = ""
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1

    for x in t:
        if x in d:
            for i in range(0, d[x]):
                res = res + x
    return res