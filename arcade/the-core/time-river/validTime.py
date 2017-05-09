def validTime(time):
    x = time.split(':')
    if len(x) != 2: return False
    try:
        for i in range(2): x[i] = int(x[i])
        if x[0] < 0 or x[0] > 23: return False
        if x[1] < 0 or x[1] > 59: return False
        return True
    except: return False