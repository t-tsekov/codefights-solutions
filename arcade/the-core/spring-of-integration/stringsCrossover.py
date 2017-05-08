def stringsCrossover(inputArray, result):
    import itertools
    pairs = itertools.combinations(inputArray,2)
    res = 0
    for i in pairs:
        check = 0
        for j in range(len(result)):
            if i[0][j] != result[j] and i[1][j] != result[j]:
                break
            else:
                check += 1
        if check == len(result):
            res += 1
    return res