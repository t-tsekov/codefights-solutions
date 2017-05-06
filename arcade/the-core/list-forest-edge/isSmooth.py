def isSmooth(arr):
    l = len(arr)
    if l % 2 == 0:
        mid = (arr[l // 2 - 1] + arr[l // 2])
    else:
        mid = arr[l // 2]

    if arr[0] == arr[-1] == mid:
        return True
    else:
        return False