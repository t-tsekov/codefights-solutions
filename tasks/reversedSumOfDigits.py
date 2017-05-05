def reversedSumOfDigits(p, n):
    if (p == 0 and n == 1):
        return "0"
    a = ""
    for i in range(1, n + 1):
        start = 1 if i == 1 else 0
        for d in range(start, 10):
            if ((n - i) * 9 + d >= p):
                a = a + str(d)
                p -= d
                break

    if (len(a) == n and p == 0):
        return a
    return "-1"
