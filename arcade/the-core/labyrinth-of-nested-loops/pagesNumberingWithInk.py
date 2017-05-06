def pagesNumberingWithInk(current, numberOfDigits):
    numberOfDigits -= len(str(current))

    while numberOfDigits >= len(str(current)):
        numberOfDigits -= len(str(current))
        current += 1

    return current