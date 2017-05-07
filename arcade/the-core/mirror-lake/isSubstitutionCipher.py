def isSubstitutionCipher(string1, string2):
    d = {}
    r = {}
    for x,y in zip(string1,string2):
        if x in d:
            if d[x]!=y:
                return 0
        if y in r:
            if r[y]!=x:
                return 0
        r[y]=x
        d[x]=y
    return 1