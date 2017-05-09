from datetime import datetime
def regularMonths(currMonth):
    mo, yr = currMonth.split('-')
    mo = int(mo)
    yr = int(yr)
    while True:
        mo += 1
        if mo == 13:
            mo = 1
            yr += 1
        if datetime(yr,mo,1).isoweekday() == True: return "{:02}-{}".format(mo,yr)