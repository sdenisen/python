import calendar
from datetime import datetime, timedelta


def split_to_intervals(start_date, end_date, interval):
    result = []
    while True:
        period = start_date
        if interval == 'WEEK':
            remains_days = 7 - period.isoweekday()
            period += timedelta(days=remains_days)
        elif interval == 'MONTH':
            remains_days = calendar.monthrange(start_date.year, start_date.month)[1]
            period = period.replace(day=remains_days)
        elif interval == 'YEAR':
            period = period.replace(day=31, month=12)
        elif interval == 'QUARTER':
            quarter1_end = datetime.strptime("2020-03-31", "%Y-%m-%d")
            quarter2_end = datetime.strptime("2020-06-30", "%Y-%m-%d")
            quarter3_end = datetime.strptime("2020-09-30", "%Y-%m-%d")
            quarter4_end = datetime.strptime("2020-12-31", "%Y-%m-%d")
            while not ((period.day == quarter1_end.day and period.month == quarter1_end.month) or
                       (period.day == quarter2_end.day and period.month == quarter2_end.month) or
                       (period.day == quarter3_end.day and period.month == quarter3_end.month) or
                       (period.day == quarter4_end.day and period.month == quarter4_end.month)):
                period += timedelta(days=1)
        elif interval == 'REVIEW':
            review1_end = datetime.strptime("2020-03-31", "%Y-%m-%d")
            review2_end = datetime.strptime("2020-09-30", "%Y-%m-%d")
            while not ((period.month == review1_end.month and period.day == review1_end.day) or
                       (period.month == review2_end.month and period.day == review2_end.day)):
                period += timedelta(days=1)
        if period < end_date:
            result.append(start_date.strftime('%Y-%m-%d') + ' ' + period.strftime('%Y-%m-%d'))
            start_date = period
            start_date += timedelta(days=1)
        else:
            result.append(start_date.strftime('%Y-%m-%d') + ' ' + end_date.strftime('%Y-%m-%d'))
            break
    return result


def main():
    interval = input()
    dates = input().split(" ")
    start = datetime.strptime(dates[0], '%Y-%m-%d')
    end = datetime.strptime(dates[1], '%Y-%m-%d')

    result_intervals = split_to_intervals(start, end, interval)

    print(len(result_intervals))
    print('\n'.join(result_intervals))


if __name__ == "__main__":
    main()
