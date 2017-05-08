def shuffledArray(shuffled):
    from itertools import combinations
    possibleSums = [sum(x) for x in combinations(shuffled,len(shuffled)-1)]
    shuffled.remove(list(x for x in shuffled if x in possibleSums)[0])
    return sorted(shuffled)
