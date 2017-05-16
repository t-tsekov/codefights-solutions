def areFollowingPatterns(strings, patterns):
    x = {}
    y = {}
    for i in range(len(strings)):
        if strings[i] not in x.keys():
            if patterns[i] in x.values():
                return False
            x[strings[i]] = []
        if patterns[i] not in x[strings[i]]:
            x[strings[i]].append(patterns[i])
        if len(x[strings[i]]) > 1:
            return False

        if patterns[i] not in y.keys():
            if strings[i] in y.values():
                return False
            y[patterns[i]] = []
        if strings[i] not in y[patterns[i]]:
            y[patterns[i]].append(strings[i])
        if len(y[patterns[i]]) > 1:
            return False

    return True
