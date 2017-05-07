def numbersGrouping(a):
    return len(a) + len(set((n-1)//10000 for n in a))