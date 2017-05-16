def commonCharacterCount2(s):
    from collections import Counter
    common = Counter(s[0])
    for i in range(1, len(s)):
        cur = Counter(s[i])
        for k in common.keys():
            if k not in cur.keys():
                common[k] = 0
            else:
                common[k] = min(common[k], cur[k])

    return sum(common.values())
