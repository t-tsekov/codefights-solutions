def ballsRearranging(balls):
    balls.sort()
    best = 0
    i = 0
    for j in range(len(balls)):
        while balls[i] <= balls[j] - len(balls):
            i += 1
        best = max(best, j - i + 1)
    return len(balls) - best

