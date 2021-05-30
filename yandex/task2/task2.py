import calendar
from datetime import datetime, timedelta

interval = input()
dates = input().split(" ")

start = datetime.strptime(dates[0], '%Y-%m-%d')
end = datetime.strptime(dates[1], '%Y-%m-%d')

result = []
while True:
    period = start
    if interval == 'WEEK':
        remains_days = 7 - period.isoweekday()
        period += timedelta(days=remains_days)
    elif interval == 'MONTH':
        remains_days = calendar.monthrange(start.year, start.month)[1]
        period = period.replace(day=remains_days)
    elif interval == 'YEAR':
        period = period.replace(day=31, month=12)
    elif interval == 'QUARTER':
        quarter1_end = datetime.strptime("2020-03-31", "%Y-%m-%d")
        quarter2_end = datetime.strptime("2020-06-30", "%Y-%m-%d")
        quarter3_end = datetime.strptime("2020-09-30", "%Y-%m-%d")
        quarter4_end = datetime.strptime("2020-12-31", "%Y-%m-%d")
        while not ((period.day == 31 and period.month == 3) or (period.day == 30 and period.month == 6)
                   or (period.day == 30 and period.month == 9) or (period.day == 31 and period.month == 12)):
            period += timedelta(days=1)
    elif interval == 'REVIEW':
        review1_end = datetime.strptime("2020-03-31", "%Y-%m-%d")
        review2_end = datetime.strptime("2020-09-30", "%Y-%m-%d")
        while not ((period.month == review1_end.month and period.day == review1_end.day)
                   or (period.month == review2_end.month and period.day == review2_end.day)):
            period += timedelta(days=1)
    if period < end:
        result.append(start.strftime('%Y-%m-%d') + ' ' + period.strftime('%Y-%m-%d'))
        start = period
        start += timedelta(days=1)
    else:
        result.append(start.strftime('%Y-%m-%d') + ' ' + end.strftime('%Y-%m-%d'))
        break

print(len(result))
print('\n'.join(result))
