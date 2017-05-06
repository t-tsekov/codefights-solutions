def candles(candlesNumber, makeNew):
    c = 0
    while candlesNumber >= makeNew:
        new = candlesNumber // makeNew
        c += new * makeNew
        candlesNumber = candlesNumber + new - makeNew * new

    c += candlesNumber
    return c