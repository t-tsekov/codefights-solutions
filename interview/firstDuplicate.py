def firstDuplicate(a):
    s = set()
    for i in range(len(a)):
        if a[i] in s:
            return a[i]
        s.add(a[i])
    return -1

