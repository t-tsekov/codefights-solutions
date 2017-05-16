from operator import xor
from functools import reduce

def findTheNumbers(a):
    t = reduce(xor, a)
    lastsetbit = t & -t

    x = y = 0
    for k in a:
        if k & lastsetbit:
            x ^= k
        else:
            y ^= k
    return [x, y] if x < y else [y, x]
