def beautifulText(inputString, l, r):
    length = len(inputString)

    for i in range(l, r + 1):
        flag = True
        for j in range(i, length, i + 1):
            if inputString[j] != ' ':
                flag = False
                break

        if flag:
            list_input = list(inputString)
            for idx, ch in enumerate(list_input):
                if (idx + 1) % (i + 1) == 0:
                    list_input[idx] = '\n'
            formatted = ''.join(list_input).split('\n')
            return len(set(map(len, formatted))) == 1

    return False