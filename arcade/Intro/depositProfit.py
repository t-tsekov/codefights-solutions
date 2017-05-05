def depositProfit(deposit, rate, threshold):
    count = 0
    while deposit < threshold:
        deposit *= 1 + rate/100
        count += 1
    return count
