def circleOfNumbers(n, firstNumber):
    x = firstNumber + n / 2
    if x >= n:
        return x - n
    else:
        return x
