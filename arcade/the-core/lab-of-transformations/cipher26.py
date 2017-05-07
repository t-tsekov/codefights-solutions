def cipher26(message):
    message = list(message)
    currsum = 0
    outmessage = ""
    while message:
        x = message.pop(0)
        outmessage += chr(97+(ord(x)-97-currsum)%26)
        currsum += ord(outmessage[-1])-97
    return outmessage