def appleBoxes(k):
    even = False
    red = 0
    yellow = 0

    for i in range(1, k + 1):

        apples = i * i
        if even:
            red += apples
        else:
            yellow += apples

        even = not even

    return red - yellow