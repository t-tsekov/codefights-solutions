def buildPalindrome(str):
    for i in range(len(str)):
        s = str + str[i::-1]
        if s == s[::-1]:
            return s
