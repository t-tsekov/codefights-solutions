def k(x):
    return int(max(str(x))) - int(min(str(x)))

def digitDifferenceSort(a):
    return sorted(a[::-1],key=k)