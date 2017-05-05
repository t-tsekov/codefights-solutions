def almostIncreasingSequence(sequence):
    flag =[]
    for i in range(len(sequence)-1):
        if sequence[i] < sequence[i+1]:
            flag.append(True)
        else:
            flag.append(False)
    counter = flag.count(False)
    if counter > 1:
        return False
    elif counter == 0:
        return True
    else:
        index = flag.index(False)
        if index == 0 or index == len(sequence)-2:
            return True
        elif sequence[index-1] < sequence[index+1] or sequence[index] < sequence[index+2]:
            return True
        else:
            return False