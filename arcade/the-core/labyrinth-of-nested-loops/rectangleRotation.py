def rectangleRotation(a, b):
    from math import sqrt
    x = (int)(a / sqrt(2))
    y = (int)(b / sqrt(2))
    if ((x + y) % 2 == 0):
        return x * y + (x + 1) * (y + 1);
    return (x + 1) * y + (y + 1) * x


