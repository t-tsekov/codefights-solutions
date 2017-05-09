def dayOfWeek(birthdayDate):
    from datetime import datetime
    a=datetime.strptime(birthdayDate,'%m-%d-%Y')
    month=str(a.month)
    day=str(a.day)
    year=int(a.year)
    weekday = a.weekday()
    count=0
    while True:
        count +=1
        year +=1
        try:
            b=datetime.strptime(month+"-"+day+"-"+str(year),'%m-%d-%Y')
            if b.weekday() == weekday:
                return count
        except ValueError:
            continue