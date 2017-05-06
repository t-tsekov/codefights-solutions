def countSumOfTwoRepresentations2(n, l, r):
    res = 0
    for a in range(l, r + 1):
        b = n - a
        if a > b:
            break
        if l <= b <= r:
            res += 1

    return res