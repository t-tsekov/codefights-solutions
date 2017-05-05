def commonCharacterCount(s1, s2):
    a = list(s1)
    b = list(s2)
    count = 0
    for c in a:
        if c in b:
            b.remove(c)
            count += 1
    return count
