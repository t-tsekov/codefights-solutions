def isInfiniteProcess(a, b):
    while a <= b:
        if a == b:
            return False
        a += 1
        b -= 1

    return True