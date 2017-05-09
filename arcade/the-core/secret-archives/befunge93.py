def befunge93(program):
    def popper(n = 1):
        return stack.pop(-n) if len(stack) >= n else 0

    def move(r, c, m = 1):
        if dr:
            r = {h: 0, -1: h - 1}.get(r + dr * m, r + dr * m)
        elif dc:
            c = {l: 0, -1: l - 1}.get(c + dc * m, c + dc * m)
        return r, c

    stack = []
    res = ''
    row = col = 0
    dr = 0
    dc = 1
    for i, v in enumerate(program):
        program[i] = v.replace('\"', "'")
    l = len(program[0])
    h = len(program)
    for _ in range(10 ** 5):
        cursor = program[row][col]
        if cursor == '@' or len(res) == 100:
            break
        if cursor in '<>':
            dc = (-1, 1)[cursor == '>']
            dr = 0
        elif cursor in '^v':
            dc = 0
            dr = (-1, 1)[cursor == 'v']
        elif cursor == '_':
            dc = (-1, 1)[not popper()]
            dr = 0
        elif cursor == '|':
            dc = 0
            dr = (-1, 1)[not popper()]
        elif cursor == '+':
            stack.append(popper() + popper())
        elif cursor == '-':
            a = popper()
            b = popper()
            stack.append(b - a)
        elif cursor == '*':
            stack.append(popper() * popper())
        elif cursor == '/':
            a = popper()
            b = popper()
            stack.append(b // a)
        elif cursor == '%':
            a = popper()
            b = popper()
            stack.append(b % a)
        elif cursor == '!':
            stack.append((0, 1)[not popper()])
        elif cursor == '`':
            a = popper()
            b = popper()
            stack.append((0, 1)[b > a])
        elif cursor == ':':
            stack.append(stack[-1] if stack else 0)
        elif cursor == '\\':
            stack.append(popper(2))
        elif cursor == '$':
            stack.pop()
        elif cursor == '.':
            res += str(popper()) + ' '
        elif cursor == ',':
            res += chr(popper())
        elif cursor.isdigit():
            stack.append(int(cursor))
        elif cursor == "'":
            row, col = move(row, col)
            while program[row][col] != "'":
                stack.append(ord(program[row][col]))
                row, col = move(row, col)
        row, col = move(row, col, (1, 2)[cursor == '#'])
    return res