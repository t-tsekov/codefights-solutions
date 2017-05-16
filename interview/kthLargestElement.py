def kthLargestElement(A, k):
    k = len(A) - k
    def quick(A, start, stop):
        piv, L, R = A[start], start, stop
        if start >= stop: return
        while L <= R:
            while A[L] < piv: L += 1
            while A[R] > piv: R -= 1
            if L <= R:
                A[L], A[R] = A[R], A[L]
                L += 1
                R -= 1
        if R >= k:
            quick(A, start, R)
        else:
            quick(A, L, stop)
    quick(A, 0, len(A) - 1)
    return A[k]