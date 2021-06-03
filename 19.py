# Counting Sundays
import datetime
import time

def loop_through_days():
    start_date = datetime.date(1901,1,1)
    end_date = datetime.date(2000,12,31)
    delta = datetime.timedelta(days=1)

    counter = 0
    while start_date <= end_date:
        # print(start_date)
        if start_date.weekday() == 6 and start_date.day == 1:
            counter += 1
        start_date += delta
    return counter

start_time = time.time()

result = loop_through_days()
print(result)

print(time.time() - start_time)