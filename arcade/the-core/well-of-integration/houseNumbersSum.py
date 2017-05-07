def houseNumbersSum(inputArray):
    sum = 0
    for i in range(len(inputArray)):
        if inputArray[i] != 0:
            sum += inputArray[i]
        else:
            break
    return sum

