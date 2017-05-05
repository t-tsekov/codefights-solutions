def longestDigitsPrefix(inputString):
    i = 0
    curr = 0
    for i in range(len(inputString)):
        if not inputString[i].isdigit():
            curr = i
            break
        if i == len(inputString) - 1:
            curr = i + 1

    return inputString[:curr]