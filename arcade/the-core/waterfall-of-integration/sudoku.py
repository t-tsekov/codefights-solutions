def sudoku(grid):
    def row(r):
        return grid[r]
    def column(c):
        return [grid[k][c] for k in range(9)]
    def block(r, c):
        return sum((grid[q][3*c:3*c+3] for q in range(3*r,3*r+3)),[])
    if any(len(set(row(r)))<9 for r in range(9)):
        return False
    if any(len(set(column(c)))<9 for c in range(9)):
        return False
    if any(len(set(block(r,c)))<9 for r in range(3) for c in range(3)):
        return False
    return True