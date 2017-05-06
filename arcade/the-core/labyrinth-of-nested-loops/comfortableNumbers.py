def comfortableNumbers(L, R):
    if R <= L:
        return 0

    count = 0

    for a in range(L, R):
        sum_a = sum_digits(a)
        for b in range(L + 1, R + 1):
            if a >= b:
                continue

            sum_b = sum_digits(b)
            if ((b <= a + sum_a) and (a >= b - sum_b)):
                count += 1;

    return count


def sum_digits(n):
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r
