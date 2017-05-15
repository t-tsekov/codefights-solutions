def strstr(s, x):
    lenx = len(x)
    for i in range(len(s)-lenx+1):
        if s[i:i+lenx] == x:
            return i
    return -1