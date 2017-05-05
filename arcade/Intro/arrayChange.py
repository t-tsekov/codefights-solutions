def arrayChange(inputArray):
    count  = 0
    for i in range(1, len(inputArray)):
        if inputArray[i] <= inputArray[i-1]:
            diff = inputArray[i-1] - inputArray[i]
            inputArray[i] += diff + 1
            count += diff + 1
    return count