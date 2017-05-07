def houseOfCats(legs):
    res = []
    while legs >= 0:
        res.insert(0, legs // 2)
        legs += -4

    return res
