def constructSquare(s):
    length = len(s)
    distinct = len(set(list(s)))

    counts = sorted([s.count(char) for char in set(list(s))])

    i = 1

    while len(str(i * i)) < length:
        i += 1

    vals = []
    while (len(str(i * i)) == length):
        if len(set(list(str(i * i)))) == distinct:
            number = str(i * i)
            counts2 = sorted([number.count(char) for char in set(list(number))])
            if counts == counts2:
                vals.append(i * i)
        i += 1
    return -1 if vals == [] else max(vals)