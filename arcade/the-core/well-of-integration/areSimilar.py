def areSimilar(A, B):
    if A == B:
        return True
    differ = []
    for i in range(len(A)):
        if A[i] != B[i]:
            differ.append(i)
            if len(differ) > 2:
                return False
    if len(differ) == 1:
        return False

    return (B[differ[0]], B[differ[1]]) == (A[differ[1]], A[differ[0]]) 