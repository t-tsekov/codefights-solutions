import datetime
def curiousClock(someTime, leavingTime):
    return str(datetime.datetime.strptime(someTime, '%Y-%m-%d %H:%M')
               - (datetime.datetime.strptime(leavingTime, '%Y-%m-%d %H:%M')
                  - datetime.datetime.strptime(someTime, '%Y-%m-%d %H:%M')))[:-3]

