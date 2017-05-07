def minimalNumberOfCoins(coins, price):
    s = 0
    for i in coins[::-1]:
        while price >= i:
            price -= i
            s += 1
    return s