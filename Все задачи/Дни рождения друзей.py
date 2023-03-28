import datetime as dt
now, interval = dt.datetime.now(), dt.timedelta(int(input()))
result = now + interval
print(result.day, result.month)
