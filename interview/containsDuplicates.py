def containsDuplicates(a):
    s = set()
    for x in a:
        if x in s:
            return True
        s.add(x)

    return False

