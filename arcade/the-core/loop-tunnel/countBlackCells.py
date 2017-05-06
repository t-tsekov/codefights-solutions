def countBlackCells(n, m):
    from fractions import gcd
    if n !=m:
        return m + n  - gcd(m,n) + (gcd(m,n) - 1) * 2
    else:
        return 4 + (n-2)*3

