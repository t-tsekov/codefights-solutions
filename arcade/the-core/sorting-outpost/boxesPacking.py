def boxesPacking(length, width, height):

    boxes = sorted(map(sorted, zip(length,width,height)))
    for (x1,y1,z1),(x2,y2,z2) in zip(boxes,boxes[1:]):
        if x1 >= x2 or y1 >= y2 or z1 >= z2:
            return False
    return True