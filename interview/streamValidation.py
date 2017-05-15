def streamValidation(stream):
    for i in range(len(stream)):
        stream[i] = bin(stream[i])[2:]
        stream[i] = '0' * (8 - len(stream[i])) + stream[i]
    i = 0

    while i < len(stream):
        if stream[i][0] == '1':
            j = 0
            while j < 8 and stream[i][j] == '1':
                j += 1
            j -= 1
            if j == 0:
                return False
            i += 1
            while i < len(stream) and j != 0:
                j -= 1
                if stream[i][:2] != '10':
                    return False
                i += 1
            if i == len(stream) and j != 0:
                return False
        else:
            i += 1
    return True