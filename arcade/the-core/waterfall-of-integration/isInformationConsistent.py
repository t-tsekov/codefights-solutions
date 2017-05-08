def isInformationConsistent(evidences):
    for x in range(len(evidences[0])):
        c = [evidences[i][x] for i in range(len(evidences))]
        if 1 in c and -1 in c:
            return False
    return True
