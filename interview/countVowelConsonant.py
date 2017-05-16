def countVowelConsonant(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    sum = 0
    for c in s:
        if c in vowels:
            sum+= 1
        else:
            sum += 2
    return sum

