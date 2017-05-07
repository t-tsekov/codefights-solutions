def reflectString(inputString):
    return inputString.translate(str.maketrans(string.ascii_lowercase, string.ascii_lowercase[::-1]))

