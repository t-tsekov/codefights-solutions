def characterParity(symbol):
    if not symbol.isdigit():
        return "not a digit"
    if int(symbol) % 2 == 0:
        return "even"
    return "odd"
