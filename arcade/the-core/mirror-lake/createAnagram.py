def createAnagram(s, t):
    cs = {c: s.count(c) for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
    res = 0
    for c in t:
        if cs[c]:
            cs[c] -= 1
        else:
            res += 1
    return res

