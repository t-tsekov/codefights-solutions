def groupsOfAnagrams(words):
    words = [str(sorted(w)) for w in words]
    c = 0
    unique = set()
    for w in words:
        if w not in unique:
            c += 1
        unique.add(w)
    return c

