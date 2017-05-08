def combs(comb1, comb2):
    res = len(comb1) + len(comb2)
    check = comb1 + ('.' * len(comb2))
    print(check)
    for i in range(len(check)):
        match = True
        pairs = 0
        if i >= len(comb1):
            pairs = len(comb2) - ((i+1) - len(comb1))
        elif (i + 1) > len(comb2):
            pairs = len(comb2)
        else:
            pairs = i + 1
        count = i
        c2 = -1
        while count >= 0 and abs(c2) <= len(comb2):
            if check[count] == '*' and comb2[c2] == '*':
                match = False
            count -= 1
            c2 -= 1
        if match == True:
            if pairs > len(comb2):
                pairs = len(comb2)
            length = len(comb1) + len(comb2) - pairs
            if length < res:
                res = length
    return res