def areSimilar(a, b):
    c = 0
    ele = []
    for i in range(len(a)):
        if a[i] != b[i]:
            c+= 1
            if c > 2:
                return False
            ele.append([a[i], b[i]])
    if c == 1:
        return False
    if c == 0:
        return True
    if ele[0][0] != ele[1][1] or ele[0][1] != ele[1][0]:
        return False
    return True