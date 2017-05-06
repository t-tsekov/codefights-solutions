def phoneCall(min1, min2_10, min11, s):
    mins = 0
    cost = min1
    while True:
        s -= cost
        if s < 0:
            break
        else:
            mins += 1
            if mins > 0 and mins < 10:
                cost = min2_10
            else:
                cost = min11
    return mins