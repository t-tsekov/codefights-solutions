def additionWithoutCarrying(param1, param2):
    i, temp = 10, 0
    total = param1 + param2
    while param1 or param2:
        if (param1 % 10) + (param2 % 10) > 9: temp += i
        param1, param2, i = param1 // 10, param2 // 10, i * 10

    return total - temp
