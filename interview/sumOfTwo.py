def sumOfTwo(a, b, v):
    a = sorted(a)
    b = sorted(b)
    l1 = len(a)
    l2 = len(b)
    x = 0
    y = l2 - 1
    while x < l1:
        while y > 0:
            if a[x] + b[y] < v:
                break
            if a[x] + b[y] == v:
                return 1
            y -= 1
            if y < 0:
                return 0
        if a[x] + b[y] > v:
            break
        x+=1
    return 0