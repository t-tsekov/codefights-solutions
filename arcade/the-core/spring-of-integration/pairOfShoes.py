def pairOfShoes(shoes):
    a = 101*[0]
    for type, size in shoes:
        if type == 0:
            a[size] -= 1
        else:
            a[size] += 1
    return not any(a)  