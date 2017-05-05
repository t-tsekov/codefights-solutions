def chessBoardCellColor(cell1, cell2):
    c1 = [ord(cell1[0])-96,int(cell1[1])]
    c2 = [ord(cell2[0])-96,int(cell2[1])]
    return (c1[0]+c1[1])%2==(c2[0]+c2[1])%2