def tripletSum(b, a):
    a.sort()
    for i in range(0, len(a) - 2):
        x = a[i]
        y = i + 1
        z = len(a) - 1
        while y < z:
            triplet_sum = x + a[y] + a[z]
            if triplet_sum == b:
                return True
            elif triplet_sum < b:
                y += 1
            else:
                z -= 1
    return False
