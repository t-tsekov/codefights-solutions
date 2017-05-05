def isBeautifulString(inputString):
    a = sorted(set(inputString))
    for i in range(1, len(a)):
        if(inputString.count(a[i]) > inputString.count(a[i - 1])):
            return False
    return a[0] == 'a'