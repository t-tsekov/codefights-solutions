def textJustification(words, L):
    begin, end = 0, 0
    result = []

    while True:
        wordsLen = 0
        while end < len(words):
            if wordsLen + len(words[end]) + (end - begin) <= L:
                wordsLen += len(words[end])
                end += 1
            else:
                break
        else:
            temp = " ".join(words[begin:end])
            temp += " " * (L - len(temp))
            result.append(temp)
            break

        temp = ""
        if end == begin + 1:
            temp = words[begin] + " " * (L - len(words[begin]))
        else:
            spaceCount = (L - wordsLen) // (end - begin - 1)
            oneMoreSpace = (L - wordsLen) % (end - begin - 1)

            for index in range(begin, end - 1):
                if index - begin < oneMoreSpace:
                    temp += words[index] + " " * (spaceCount + 1)
                else:
                    temp += words[index] + " " * spaceCount
            temp += words[end - 1]

        result.append(temp)
        begin = end

    return result
