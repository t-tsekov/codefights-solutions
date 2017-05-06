def isTandemRepeat(inputString):
    l = len(inputString)
    if l % 2 != 0:
        return False
    if inputString[:l // 2] != inputString[l // 2:]:
        return False

    return True
