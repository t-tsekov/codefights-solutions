def sortByHeight(a):
    b = [x for x in a]
    a = sorted(list(filter(lambda x:x!= -1, a)))
    index = 0
    for i in range(len(a)):
        while True:
            if b[index] == -1 and index < len(b):
                index += 1
            else:
                b[index] = a[i]
                index += 1
                break

    return b