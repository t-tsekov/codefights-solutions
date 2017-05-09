def bishopDiagonal(bishop1, bishop2):
    cols = 'abcdefgh'
    rows = '12345678'

    def bishopMoves(cell):
        col, row = cols.index(cell[0]), rows.index(cell[1])
        for c in range(8):
            for r in (row - (col - c), row - (c - col)):
                if 0 <= r < 8:
                    yield cols[c] + rows[r]

    b1 = set(bishopMoves(bishop1))
    b2 = set(bishopMoves(bishop2))
    u = b1.intersection(b2)
    if len(u) == 0:
        return sorted([bishop1, bishop2])
    else:
        s = sorted(u, reverse = bishop2 < bishop1)
        return sorted([s[0], s[-1]])
