def differentRightmostBit(n, m):
    return -~((~(n^m))^((~(n^m))+1))>>1