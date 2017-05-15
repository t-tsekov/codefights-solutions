def reverseVowelsOfString(s):
    vowels = "aeiouAEIOU"
    s = list(s)
    front, end = 0, len(s) - 1
    move_front = True
    while front <= end:
        if s[front] in vowels and s[end] in vowels:
            s[front], s[end] = s[end], s[front]
            front += 1
            end -= 1
        elif s[front] in vowels:
            end -= 1
        else:
            front += 1

    return "".join(s)
