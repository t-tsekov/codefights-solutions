def chessTriangle(n, m):
    return max(0, 8*(n-1)*(m-2)) + max(0, 8*(n-2)*(m-1)) + \
           max(0, 16*(n-2)*(m-2)) + max(0, 8*(n-2)*(m-3)) + \
           max(0, 8*(n-3)*(m-2)) + max(0, 8*(n-1)*(m-3)) + max(0, 8*(n-3)*(m-1))