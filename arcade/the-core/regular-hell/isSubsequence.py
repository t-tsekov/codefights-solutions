def isSubsequence(t, s):
    pattern = ''
    for ch in s :
        pattern += ".*"+ re.escape(ch)
    return re.search(pattern, t) is not None
