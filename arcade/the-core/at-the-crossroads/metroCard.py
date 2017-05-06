def metroCard(lastNumberOfDays):
    a = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    b = set()
    for i in range(11):
        if a[i] == lastNumberOfDays:
            b.add(a[i + 1])

    return sorted(list(b))