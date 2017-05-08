def cyclicString(s):
    end = 1
    pattern = True
    while end < len(s):
        for i in range(len(s)-end):
            if s[i+end] != s[i%end]:
                pattern = False
                continue
        if pattern == True:
            return end
        pattern = True
        end +=1
    return end