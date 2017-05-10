def primesSum(a, b):
    return sum([x for x in range(a,b+1) if all(x % i for i in range(2, int(x**0.5 + 1))) and x!= 1])
