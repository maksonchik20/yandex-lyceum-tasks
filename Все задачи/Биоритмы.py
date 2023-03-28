import datetime as dt
from math import sin, pi


def bioritm(T, P):
    return round(sin((2 * pi * T) / P) * 100, 2)


day, month, year  = map(int, input().split('.'))
to_day, to_month, to_year = map(int, input().split('.'))
T = (dt.datetime(to_year, to_month, to_day) - dt.datetime(year, month, day)).total_seconds() / 86400
print(bioritm(T, 23), bioritm(T, 28), bioritm(T, 33), sep="\n")
