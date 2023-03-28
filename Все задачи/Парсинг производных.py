from math import log
s = input()
d = int(input())

if s[0] == "x":
    a = int(s[s.index('^') + 1:])
    print(a * (d ** (a - 1)))
elif s[0].isdigit():
    a = int(s[:s.index('^')])
    print(round(log(a) * (a ** d), 3))