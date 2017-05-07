def addBorder(picture):
    res = ['*' * (len(picture[0]) + 2)]
    for i in picture:
        res.append('*' + i + '*')
    res.append('*' * (len(picture[0]) + 2))
    return res