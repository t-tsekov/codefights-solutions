from itertools import permutations

def kthPermutation(numbers, k):
    return sorted(list(permutations(numbers)))[k-1]
