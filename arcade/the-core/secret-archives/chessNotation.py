def chessNotation(notation):
    board = []
    for line in notation.split('/'):
        buf = []
        for k in line:
            if not k.isdigit():
                buf.append(k)
            else:
                for _ in xrange(int(k)):
                    buf.append(" ")
        board.append(buf)

    from itertools import groupby
    def cvt(line):
        ans = ''
        for k, v in groupby(line, lambda x: x == ' '):
            if k:
                l = len(list(v))
                ans += str(l)
            else:
                for u in v:
                    ans += u
        return ans

    board = [col[::-1] for col in zip(*board)]
    return "/".join(cvt(line) for line in board)