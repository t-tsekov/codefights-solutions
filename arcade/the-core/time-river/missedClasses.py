from datetime import datetime

def missedClasses(year, daysOfTheWeek, holidays):
    def cvt(d):
        return map(int, d.split('-'))

    holidays = map(cvt, holidays)
    ans = 0
    for mo, day in holidays:
        x = datetime(year + (mo < 6), mo, day)
        if x.isoweekday() in daysOfTheWeek: ans += 1
    return ans
