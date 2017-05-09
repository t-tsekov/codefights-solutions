import datetime

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def holiday(x, weekDay, month, yearNumber):
    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_num = months.index(month) + 1
    first_of_month = datetime.date(yearNumber, month_num, 1)
    day_of_week = first_of_month.weekday()
    weekday_num = days.index(weekDay)
    day = (weekday_num - day_of_week) % 7

    day = day + 7 * (x - 1)
    final_date = datetime.date(yearNumber, month_num, 1) + datetime.timedelta(days = day)
    print(str(final_date))
    if final_date.month != month_num:
        return -1
    else:
        return final_date.day

