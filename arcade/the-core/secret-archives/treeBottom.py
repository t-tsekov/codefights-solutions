def treeBottom(tree):
    deep = 0
    maxDeep = 0
    res = []
    num = []
    for c in tree:
        if c == '(':
            deep += 1
        elif c == ')':
            deep -= 1
        elif c.isdigit():
            if deep > maxDeep:
                maxDeep = deep
                res = []
            if deep == maxDeep:
                num.append(c)
        elif c == ' ' and num:
            res.append(int(''.join(num)))
            num = []

    return res