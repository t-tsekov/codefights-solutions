def whoseTurn(p):
    return sum(map(ord,p[:2]+p[3:5]))%2==sum(map(ord,p[6:8]+p[9:11]))%2