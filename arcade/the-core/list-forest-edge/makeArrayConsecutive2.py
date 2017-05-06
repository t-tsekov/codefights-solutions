def makeArrayConsecutive2(sequence):
    min_num = min(sequence)
    max_num = max(sequence)
    count = 0
    for i in range(min_num + 1, max_num):
        if i not in sequence:
            count += 1

    return count