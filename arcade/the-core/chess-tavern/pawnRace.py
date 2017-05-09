def pawnRace(white, black, toMove):
    x1, y1, x2, y2 = ord(white[0])-97, ord(white[1])-49, ord(black[0])-97, ord(black[1])-49
    flip = toMove == "b"
    if flip:
        x1, y1, x2, y2 = x2, 7-y2, x1, 7-y1
    if abs(x1-x2) >= 4 or y1 >= y2:
        r = 1 if 7-max(y1, 2) <= min(y2, 5) else -1
    elif x1 == x2:
        r = 0
    elif y2 == 6 and y1 < 3 or y1 > 1 and (y1^y2)%2 == 0:
        r = -1
    else:
        r = 1
    return ["white", "draw", "black"][1+r if flip else 1-r]