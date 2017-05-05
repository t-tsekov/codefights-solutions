from statistics import median

def absoluteValuesSumMinimization(a):

    med = median(a)
    return min(a, key = lambda x: abs(med - x))