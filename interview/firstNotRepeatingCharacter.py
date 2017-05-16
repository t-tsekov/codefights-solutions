def firstNotRepeatingCharacter(s):
    nr = []
    r = set()
    for c in s:
        if c not in r:
            nr.append(c)
            r.add(c)
        elif c in nr:
            nr.remove(c)

    if len(nr) > 0:
        return nr[0]
    else:
        return "_"

