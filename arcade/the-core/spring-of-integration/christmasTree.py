def christmasTree(levelNum, levelHeight):
    lines = ["*", "*", "***"]
    for l in range(levelNum):
        sw = 5 + 2 * l
        for h in range(levelHeight):
            w = sw + 2 * h
            lines.append("*" * w)
    lines.extend(["*" * (levelHeight + (levelHeight+1) % 2)] * levelNum)
    pad = lambda l: "{:^{}s}".format(l, w).rstrip()
    return [pad(l) for l in lines]