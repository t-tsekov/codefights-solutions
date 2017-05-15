def repeatedDNASequences(s):
    n = len(s)
    res = set()
    for i in range(n - 10):
        cur = s[i:i + 10]
        if cur in s[i + 1:]:
            res.add(cur)

    return sorted(res)
