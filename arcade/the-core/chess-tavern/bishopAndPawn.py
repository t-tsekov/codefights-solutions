def bishopAndPawn(bishop, pawn):
    x = 'abcdefgh'
    b_loc = [x.index(bishop[0] + 1), int(bishop[1])]
    p_loc = [x.index(pawn[0] + 1), int(pawn[1])]
    return abs(b_loc[0] - p_loc[0]) == abs(b_loc[1] - p_loc[1])
