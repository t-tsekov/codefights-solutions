def stringPermutations(s):
    res = set()
    permute(list(s), 0, len(s) -1, res)
    return sorted(res)

def permute(a, l, r, s):
    if l==r:
        s.add(''.join(a))
    else:
        for i in range(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r, s)
            a[l], a[i] = a[i], a[l] # backtrack
