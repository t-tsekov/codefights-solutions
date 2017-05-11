class Prizes(object):
    def __init__(self, purchases, n, d):

        self.purchases = purchases
        self.n = n
        self.d = d
        self.l = len(purchases)
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.l:
            for i in range(self.i, self.l):
                if (i + 1) % self.n == 0 and self.purchases[i] % self.d == 0:
                    self.i = i + 1
                    return i + 1
            raise StopIteration
        else:
            raise StopIteration


def superPrize(purchases, n, d):
    return list(Prizes(purchases, n, d))