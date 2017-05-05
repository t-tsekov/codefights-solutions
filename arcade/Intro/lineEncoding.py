def lineEncoding(s):
    res = ''
    prev = ''
    count = 1
    for ch in s:
        if ch == prev:
            count += 1
        else:
            if prev:
                if count == 1:
                    res += prev
                else:
                    res += str(count)+prev
                count = 1
        prev = ch
    if count ==1:
        res += prev
    else:
        res += str(count)+prev
    return res