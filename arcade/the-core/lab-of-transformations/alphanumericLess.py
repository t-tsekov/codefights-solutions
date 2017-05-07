def alphanumericLess(s1, s2):
    s1 = tokenize(s1)
    s2 = tokenize(s2)

    for i in range(min(len(s1), len(s2))):
        if s1[i].isdigit():
            if s2[i].isdigit():
                if int(s1[i]) < int(s2[i]):
                    return True
            else:
                return True
        else:
            if s2[i].isdigit():
                pass
            elif s1[i] < s2[i]:
                return True

    if len(s1) < len(s2):
        return True
    if len(s1) > len(s2):
        return False
    for i in range(len(s1)):
        if s1[i].isdigit():
            if len(s1[i]) > len(s2[i]):
                return True
    return False


def tokenize(string):
    token = []
    temp = []
    for i in range(len(string)):
        temp += [string[i]]
        if i + 1 == len(string) or string[i].isalpha() or string[i + 1].isalpha():
            token += [''.join(temp)]
            temp = []
    return token