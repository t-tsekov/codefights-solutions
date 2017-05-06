def isSumOfConsecutive2(n):
    count = 0
    for i in range(1, 25):
        sum = 0
        x = i
        while sum < n:
            sum += x
            x += 1

        if sum == n and n != i:
            count += 1

    return count