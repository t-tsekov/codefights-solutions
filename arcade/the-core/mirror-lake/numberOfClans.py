def numberOfClans(divisors, k):
    divisors = set(divisors)
    d = []
    for n in range(1, k + 1, 1):
        sd = []
        for div in divisors:
            if n % div == 0:
                sd.append(div)
        if sd == []:
            sd = [1]
        if sd not in d:
            d.append(sd)

    return len(d)
