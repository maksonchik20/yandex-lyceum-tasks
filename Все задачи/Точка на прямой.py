def line(s, t):
    x, y = map(float, t.split(';'))
    if '+' in s[s.index('x') + 1:] and float(s[:s.index('x')]) * x + float(s[s.index('+') + 1:]) == y:
        print('True')
    elif s[0] == '-':
        if float(s[:s.index('x')]) * x + float(s[s.index('x') + 1:][s.index('-'):]) == y:
            print('True')
        else:
            print('False')
    else:
        print('False')

line("3.5x+0", "2;7")
line("5x-10", "5;-9")
line("-0.24x-9.4", "8.6;-11.464")