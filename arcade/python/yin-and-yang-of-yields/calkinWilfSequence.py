def calkinWilfSequence(number):
    def fractions():
        n = 1
        d = 1
        yield [n, d]
        while True:
            n, d = d, 2 * (n // d) * d + d - n
            yield [n, d]

    gen = fractions()
    res = 0
    while next(gen) != number:
        res += 1
    return res
