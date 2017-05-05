def palindromeRearranging(inputString):
    from collections import Counter
    c = Counter(inputString)
    flag = False
    for v in c.values():
        if v % 2 != 0:
            if flag == False:
                flag = True
            else:
                return False
    return True