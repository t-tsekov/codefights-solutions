def amazonCheckmate(king, amazon):
    cols = 'abcdefgh'
    rows = '12345678'

    def parse(cell):
        return cols.index(cell[0]), rows.index(cell[1])

    def moves(cell, piece):
        return set(m for m in _moves(cell, piece) if m not in (cell, None))

    def _moves(cell, piece):
        col, row = parse(cell)

        def loc(c, r):
            if 0 <= c < 8 and 0 <= r < 8:
                l = cols[c] + rows[r]
                if l != king:
                    return l
            return None

        if piece == 'k':
            for rdiff in (-1, 0, 1):
                for cdiff in (-1, 0, 1):
                    yield loc(col + cdiff, row + rdiff)
        else:
            # knight
            for cdiff in (-2, -1, 1, 2):
                yield loc(col + cdiff, row + 3 - abs(cdiff))
                yield loc(col + cdiff, row - 3 + abs(cdiff))
            # bishop - be careful not to intersect the king
            for hdir in (-1, 1):
                for vdir in (-1, 1):
                    for diff in range(1, 8):
                        l = loc(col + hdir * diff, row + vdir * diff)
                        if not l:
                            break
                        yield l
            # rook - be careful not to intersect the king
            for hdir, vdir in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
                for diff in range(1, 8):
                    l = loc(col + hdir * diff, row + vdir * diff)
                    if not l:
                        break
                    yield l

    k = moves(king, 'k')
    a = moves(amazon, 'a')
    print('k', sorted(moves(king, 'k')))
    print('a', sorted(moves(amazon, 'a')))

    checkmate, check, stalemate, safe = set(), set(), set(), set()
    for col in cols:
        for row in rows:
            testpos = col + row
            if testpos in k or testpos in (king, amazon):
                continue  # black king cannot be within white king's range or same square as a white piece

            t = moves(testpos, 'k')

            # check to see if testpos is safe
            if testpos not in a.union(k):
                is_safe = True
            else:
                is_safe = False
