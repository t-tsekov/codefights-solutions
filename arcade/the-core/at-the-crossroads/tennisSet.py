def tennisSet(score1, score2):
    if score1 == score2:
        return False
    if score1 > 7 or score2 > 7:
        return False
    if (score1 == 7 and score2 < 5) or (score2 == 7 and score1 < 5):
        return False
    if score1 < 6 and score2 < 6:
        return False
    if (score1 == 6 and (score2 == 5 or score2 == 6)) or (score2 == 6 and (score1 == 5 or score1 == 6)):
        return False

    return True
