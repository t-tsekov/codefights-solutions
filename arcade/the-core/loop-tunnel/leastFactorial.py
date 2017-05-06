def leastFactorial(n):
    x = 2
    prod = 1

    while prod < n:
        prod *= x
        x += 1

    return prod