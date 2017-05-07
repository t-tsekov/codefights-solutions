def decipher(cipher):
    current = 0
    result = ''
    for number in cipher:
        current = 10*current + int(number)
        if current > 96:
            result += chr(current)
            current = 0
    return result