def uniqueDigitProducts(a):
    return len(set([digit_prod(x) for x in a]))

def digit_prod(x):
    res = 1
    for ch in str(x):
        res *= int(ch)

    return res