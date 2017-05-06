def isMAC48Address(inputString):
    parts = inputString.lower().split("-")
    valid = "abcdef1234567890"
    if len(parts) != 6:
        return False

    for part in parts:
        if len(part) != 2:
            return False
        for n in part:
            if n not in valid:
                return False

    return True
