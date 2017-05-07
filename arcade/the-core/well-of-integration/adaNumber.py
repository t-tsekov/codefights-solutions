def adaNumber(line):
    line=line.replace('_', '')
    if '#' in line:
        try:
            base, val, __=line.split('#')
            base=int(base)
        except:
            return False
        if base>16 or base<2:
            return False
        try:
            v =int(val, base)
        except:
            return False
        return True
    if line.isnumeric():
        return True
    return False