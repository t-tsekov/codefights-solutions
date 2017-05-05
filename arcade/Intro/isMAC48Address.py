def isMAC48Address(inputString):
    groups = inputString.split("-")
    if len(groups) != 6:
        return False
    valid = "ABCDEFabcdef"
    for g in groups:
        if len(g) != 2:
            return False
        for c in g:
            if not (c.isdigit() or c in valid):
                return False

    return True