def squareDigitsSequence(a0):
    l = []

    l.append(a0)

    while True:
        sq_sum = sum([int(num) ** 2 for num in str(l[-1])])
        if sq_sum in l:
            break
        else:
            l.append(sq_sum)

    return len(l) + 1
