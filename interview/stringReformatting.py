def stringReformatting(s, k):
    s = s.replace("-", "")
    first = len(s) % k
    res = ""
    if first != 0:
        res += s[:first] + "-"
        s = s[first:]

    for i in range(len(s)):
        res += s[i]
        if (i + 1) % k == 0:
            res += "-"

    return res[:-1]
