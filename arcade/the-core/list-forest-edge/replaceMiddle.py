def replaceMiddle(arr):
    l = len(arr)
    if l % 2 == 0:
        mid = (arr[l // 2 - 1] + arr[l // 2])
        arr.pop(l//2 - 1)
        arr[l//2 -1] = mid
    return arr