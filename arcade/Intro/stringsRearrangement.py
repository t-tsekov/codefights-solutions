import itertools

def stringsRearrangement(inputArray):
    perms_gen = itertools.permutations(inputArray)
    for perm in perms_gen:
        permstillgood = True
        for i in range(len(perm)-1):
            diff = 0
            for j in range(len(perm[i])):
                if perm[i][j] != perm[i+1][j]:
                    diff += 1
                if diff > 1:
                    permstillgood = False
                    break
            if diff != 1:
                permstillgood = False
            if not permstillgood:
                break
        else:
            return True
    return False