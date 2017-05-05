def isLucky(n):
    n = str(n)
    return sum(list(map(int, n[len(n)//2:]))) == sum(list(map(int, n[:len(n)//2])))
