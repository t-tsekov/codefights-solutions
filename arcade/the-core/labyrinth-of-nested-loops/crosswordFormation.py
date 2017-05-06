import itertools

def crosswordFormation(words):

    def numOfWays(top, bottom, left, right):
        ans1 = 0
        for i in range(len(top) - 1):
            for j in range(i + 2, len(top)):
                for shift in range(j - len(bottom) + 1, i + 1):
                    is1 = bottom[i - shift]
                    is2 = bottom[j - shift]
                    for l in range(1, min(len(left), len(right)) - 1):
                        ansl = 0
                        ansr = 0
                        for k1 in range(len(left) - l - 1):
                            k2 = k1 + l + 1
                            if top[i] == left[k1] and is1 == left[k2]:
                                ansl += 1
                        for k1 in range(len(right) - l - 1):
                            k2 = k1 + l + 1
                            if top[j] == right[k1] and is2 == right[k2]:
                                ansr += 1
                        ans1 += ansl * ansr
        return ans1

    ans = 0
    for i in range(4):
        for j in range(i + 1, 4):
            other = [0, 0]
            c = 0
            for k in range(4):
                if k != i and k != j:
                    other[c] = k
                    c += 1
            x, y = other[0], other[1]
            ans += (numOfWays(words[i], words[j], words[x], words[y])
                + numOfWays(words[j], words[i], words[x], words[y])
                + numOfWays(words[i], words[j], words[y], words[x])
                + numOfWays(words[j], words[i], words[y], words[x]))
    return ans
