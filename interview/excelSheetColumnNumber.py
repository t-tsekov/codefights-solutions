def excelSheetColumnNumber(s):
    r = 0
    for i in range(len(s)):
        r = r * 26 + ord(s[i]) - ord('A') + 1
    return r
