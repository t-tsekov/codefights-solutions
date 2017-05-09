def countElements(inputString):
    inputString = inputString.replace("[", "")
    inputString = inputString.replace("]", "")
    inString = False
    count = 1 if len(inputString) > 0 else 0
    for char in inputString:
        if char == '"':
            inString = not inString
        if not inString and char == ",":
            count += 1
    return count