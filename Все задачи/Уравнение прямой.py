def equation(a, b):
    x1, y1 = map(float, a.split(';'))
    x2, y2 = map(float, b.split(';'))
    if x1 == x2:
        print(x1)
    else:
        if y1 == y2:
            print(y1)
        else:
            print((y2 - y1) / (x2 - x1), y2 - (y2 - y1) / (x2 - x1) * x2)

equation("4;6.9", "-5.2;6.9")