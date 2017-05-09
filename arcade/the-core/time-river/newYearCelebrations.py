def newYearCelebrations(takeOffTime, minutes):
    hours, mins = list(map(int, takeOffTime.split(":")))
    count = 0
    if hours == 0 and mins == 0:
        count += 1

    for i in range(len(minutes) - 1, 0, -1):
        minutes[i] -= minutes[i - 1]

    for x in minutes:
        for i in range(x):
            hours, mins, count = plus_one_min(hours, mins, count)

        if hours > 0:
            if hours == 1 and mins == 0:
                count += 1
            hours -= 1
        else:
            hours = 23
    if hours > 16:
        count += 1
    if count == 0:
        count += 1
    return count


def plus_one_min(hours, mins, count):
    if mins < 59:
        mins += 1
    else:
        mins = 0
        if hours < 23:
            hours += 1
        else:
            hours = 0
            count += 1
    return hours, mins, count