def digitDegree(n):
    n = str(n)
    count = 0
    while len(n) > 1:
        n = str(sum([int(x) for x in n]))
        count += 1
    return count