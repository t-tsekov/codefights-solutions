def alphabeticShift(inputString):
    from string import ascii_lowercase
    maketrans = str.maketrans
    cipher_map = maketrans(ascii_lowercase, ascii_lowercase[1:] + ascii_lowercase[:1])
    return inputString.translate(cipher_map)