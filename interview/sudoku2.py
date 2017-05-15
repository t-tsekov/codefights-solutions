def sudoku2(grid):

    def checkBlock(block):
        sample = {"1","2","3","4","5","6","7","8","9"}
        for x in block:
            if x!= ".":
                if x not in sample:
                    return False
                else:
                    sample.remove(x)
        return True

    subgrids = []

    for i in range(3):
        subgrids.append([])
        for j in range(3):
            subgrids[i].append([])

    for i in range(9):
        horizontal = []
        vertical = []
        for j in range(9):
            horizontal.append(grid[i][j])
            vertical.append(grid[j][i])
            subgrids[i / 3][j / 3].append(grid[i][j])
        if not checkBlock(horizontal):
            return False
        if not checkBlock(vertical):
            return False

    for i in range(3):
        for j in range(3):
            if not checkBlock(subgrids[i][j]):
                return False

    return True
