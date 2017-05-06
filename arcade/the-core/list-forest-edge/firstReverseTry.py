def firstReverseTry(arr):
    if not arr:
        return []
    swap = arr[0]
    arr[0] = arr[-1]
    arr[-1] = swap
    return arr