def avoidObstacles(inputArray):
    max_num = max(inputArray)
    for i in range(1, 41):
        if i in inputArray:
            continue

        multiplier = 1
        while True:
            jump = i * multiplier
            if jump in inputArray:
                break
            if jump > max_num:
                return i
            multiplier += 1