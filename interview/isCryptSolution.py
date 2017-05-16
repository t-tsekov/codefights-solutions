def isCryptSolution(crypt, solution):
    solution = {x: y for x, y in solution}
    add1 = ""
    add2 = ""
    result = ""

    for i in range(len(crypt[0])):
        add1 += solution[crypt[0][i]]
    for i in range(len(crypt[1])):
        add2 += solution[crypt[1][i]]
    for i in range(len(crypt[2])):
        result += solution[crypt[2][i]]

    if (add1.startswith("0") and len(add1) > 1) or (add2.startswith("0") and len(add2) > 1) or (
        result.startswith("0") and len(result) > 1):
        return False
    elif int(add1) + int(add2) != int(result):
        return False
    else:
        return True