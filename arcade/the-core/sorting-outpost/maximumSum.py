def maximumSum(A, Q):
    sumCount = [0] * len(A)
    for i in range(len(Q)):
        for j in range(Q[i][0], Q[i][1] + 1):
            print (j)
            sumCount[j] += 1
    A.sort()
    sumCount.sort()
    res = 0
    for i in range(len(A)):
        res += A[i] * sumCount[i]
    return res
