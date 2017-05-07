def mostFrequentDigitSum(n):
    sums = []
    while n > 0:
        a = sum(int(x) for x in str(n))
        sums.append(a)
        n -= a
    sortcount = []
    for i in set(sums):
        sortcount.append((sums.count(i), i))
    sortcount.sort(reverse = True)
    max_sx = sortcount[0][1]
    for i in range(1, len(sortcount)):
        if sortcount[i][0] == sortcount[i - 1][0]:
            if sortcount[i][1] > max_sx:
                max_sx = sortcount[i][1]
    return max_sx

