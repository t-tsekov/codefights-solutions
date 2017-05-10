def pressureGauges(morning, evening):
    return [min(x,y) for x, y in zip(morning, evening)], [max(x,y) for x, y in zip(morning, evening)]
