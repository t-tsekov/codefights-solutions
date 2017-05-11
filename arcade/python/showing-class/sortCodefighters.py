def sortCodefighters(codefighters):
    res = [CodeFighter(*codefighter) for codefighter in codefighters]
    res.sort(reverse = True)
    return list(map(str, res))


class CodeFighter:
    def __init__(self, name, id, xp):
        self.name = name
        self.id = int(id)
        self.xp = int(xp)

    def __lt__(self, other):
        return ((self.xp, -self.id) <
                (other.xp, -other.id))

    def __str__(self):
        return self.name