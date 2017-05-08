def gravitation(A):
    B=zip(*A)
    res=[]
    for row in B:
        if not "#" in row:
            r.append(0)
        else:
            while row[0]==".":
                row=row[1:]
            r.append(sum([1 for x in row if x=="."]))
    minr = min(res)
    return [i for i,x in enumerate(res) if x==minr]