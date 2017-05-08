def rowsRearranging(m):
    s = sorted(m)
    for x in range(len(s[0])):
        for y in range(len(s)-1):
            if s[y][x]>=s[y+1][x]:
                return False
    return True
