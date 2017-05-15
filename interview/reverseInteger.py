def reverseInteger(x):
    digits = []
    negative = False
    if x < 0:
        x *= -1
        negative = True
    if x == 0:
        return 0
    while x:
        remainder = x % 10
        digits.append(str(remainder))
        x //= 10
    res = "".join(digits)
    if negative:
        res = "-"+res
    return int(res)