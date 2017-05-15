def sortedSquaredArray(array):
    s = [x ** 2 for x in array]
    n = len(array)
    head = 0
    tail = n - 1
    index = 0
    res = [0 for x in array]

    while head <= tail:

        if s[head] >= s[tail]:
            res[n - index - 1] = s[head]
            head += 1
        else:
            res[n - index - 1] = s[tail]
            tail -= 1

        index += 1

    return res