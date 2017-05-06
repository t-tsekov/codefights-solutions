def increaseNumberRoundness(n):
    n = str(n)[::-1]
    for i in range(len(n) - 1):
        if n[i] != "0":
            if n[i + 1] == "0":
                return True

    return False
