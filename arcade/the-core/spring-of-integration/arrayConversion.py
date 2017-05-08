def arrayConversion(inputArray):
    flag = True
    while len(inputArray) >= 2:
        if flag:
            inputArray = [a + b for a, b in zip(inputArray[0::2], inputArray[1::2])]
        else:
            inputArray = [a * b for a, b in zip(inputArray[0::2], inputArray[1::2])]
        flag = not(sumIter)
    return inputArray[0]