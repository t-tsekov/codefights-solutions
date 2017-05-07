def timedReading(maxLength, text):
    text = text.split(' ')
    var = "abcdefghijklmnopqrstuvwxyz"
    total = 0
    for val in text:
        while len(val) and (val[0] not in (var + var.upper())):
            val = val[1:]
        while len(val) and val[-1] not in (var + var.upper()):
            val = val[:-1]
        if 0 < len(val) <= maxLength:
            total += 1
    return total
