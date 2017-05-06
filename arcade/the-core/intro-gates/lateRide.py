def lateRide(n):
    m = n // 60
    s = n % 60
    return sum([int(x) for x in str(m)]) + sum([int(x) for x in str(s)])