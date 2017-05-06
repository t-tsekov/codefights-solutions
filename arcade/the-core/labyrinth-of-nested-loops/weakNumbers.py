def weakNumbers(n):
    divisors = [-1] * (n + 2)
    weakness = [-1] * (n + 2)
    count = 0
    divisors[1] = 1
    weakness[1] = 0
    for i in range(2, n + 1):
        divisors[i] = get_divisors(i)
        for j in range(1, i):
            if divisors[j] > divisors[i]:
                count += 1
        weakness[i] = count
        count = 0

    max_weakness = max(weakness)
    max_weakness_count = weakness.count(max_weakness)
    return [max_weakness, max_weakness_count]


def get_divisors(x):
    count = 0
    i = 1
    for i in range(1, x + 1):
        if x % i == 0:
            count += 1
    return count
