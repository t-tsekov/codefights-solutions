def newNumeralSystem(number):
    l = ord('A')
    r = ord(number)

    results = []
    while l <= r:
        results.append("{} + {}".format(chr(l), chr(r)))
        l += 1
        r -= 1

    return results