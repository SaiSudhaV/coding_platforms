from datetime import datetime, timezone

def formatted_date(d):
    months = {'01' : 'JAN', '02' : 'FEB', '03' : 'MAR', '04' : 'APR', '05' : 'MAY', '06' : 'JUN', '07' : 'JUL', '08' : 'AUG', '09' : 'SEP', '10' : 'OCT', '11' : 'NOV', '12' : 'DEC'}
    return "-".join(i for i in [d[0], months[d[1]], d[2]])

def formatted_day(s):
    days = {'0' : 'Monday', '1' : 'Tuesday', '2' : 'Wednesday', '3' : 'Thursday', '4' : 'Friday', '5' : 'Saturday', '6' : 'Sunday'}
    return days[s]

def date_day(seconds):
    elapse_date, elapse_day = datetime.fromtimestamp(seconds).date(), datetime.fromtimestamp(seconds).weekday()
    res = "-".join(i for i in reversed(str(elapse_date).split('-')))
    return " ". join(i for i in [formatted_date(res.split("-")), formatted_day(str(elapse_day))])

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        seconds = int(input())
        print(date_day(seconds))