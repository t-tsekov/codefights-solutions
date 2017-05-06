def rounders(value):
    plusone = False
    res = ""
    digits = len(str(value)) + 1
    for i in range(1, digits):
        num = int(str(value)[-i]) + plusone

        if i != digits - 1:
            res += "0"
        else:
            if num != 10:
                res += str(num)
            else:
                res += "01"

        if num >= 5:
            plusone = True
        else:
            plusone = False

    return int(res[::-1])