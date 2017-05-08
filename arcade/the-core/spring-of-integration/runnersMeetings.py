def runnersMeetings(startPosition, speed):

    result = -1

    for i in range(len(startPosition)):
        for j in range(i + 1, len(startPosition)):
            distDiff = startPosition[j] - startPosition[i]
            speedDiff = speed[i] - speed[j]
            cnt = 0

            if distDiff * speedDiff <= 0:
                continue

            for k in range(len(startPosition)):
                if (startPosition[k] * speedDiff + speed[k] * distDiff
                        == startPosition[i] * speedDiff + speed[i] * distDiff):
                    cnt += 1

            if cnt > result:
                result = cnt

    return result