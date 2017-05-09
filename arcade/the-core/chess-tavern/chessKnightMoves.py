def chessKnightMoves(c):
    x = ord(c[0])-ord('a')
    y = ord(c[1])-ord('1')
    def v(x,y):
        return x>=0 and y>=0 and x<8 and y<8
    s=0
    for i in range(-2,3):
        for j in range(-2,3):
            if abs(i*j) == 2:
                if v(x+i,y+j): s+=1
    return s
