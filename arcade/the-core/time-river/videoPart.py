def videoPart(part, total):
    from fractions import gcd
    def get_sec(time_str):
        h, m, s = time_str.split(':')
        return int(h) * 3600 + int(m) * 60 + int(s)
    part = get_sec(part)
    total = get_sec(total)
    x = gcd(part,total)
    return [part//x,total//x]