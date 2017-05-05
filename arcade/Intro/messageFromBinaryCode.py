def messageFromBinaryCode(code):
    res = ''
    for i in range(0,len(code),8):
        res+=chr(int(code[i:i+8], 2))
    return res