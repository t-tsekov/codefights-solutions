def stolenLunch(note):
    decrypted_message = ''

    for c in note:
        if 'a' <= c <= 'j':
            decrypted_message += str((ord(c) - ord('a')))
        elif c.isdigit():
            decrypted_message += chr(ord('a') + int(c))
        else:
            decrypted_message += c
    return decrypted_message 