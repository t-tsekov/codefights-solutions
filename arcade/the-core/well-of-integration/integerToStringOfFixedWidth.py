def integerToStringOfFixedWidth(number, width):
    if width <= len(str(number)):
        return str(number)[-width:]
    else:
        return '0' * (width - len(str(number))) + str(number)