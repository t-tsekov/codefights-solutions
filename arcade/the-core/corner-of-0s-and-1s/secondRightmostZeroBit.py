def secondRightmostZeroBit(n):
    return -~((n-~(n^(n+1))/2)^(n-~(n^(n+1))/2+1))>>1