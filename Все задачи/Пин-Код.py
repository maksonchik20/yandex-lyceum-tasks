def check_pin(pin):
    a, b, c = map(int, pin.split('-'))
    if a == 1:
        return "Некорректен"
    for i in range(2, a):
        if a % i == 0:
            return "Некорректен"
    if str(b) != str(b)[::-1]:
        return "Некорректен"
    p = 2
    flag = False
    if c != 1:
        while p <= c:
            if p == c:
                flag = True
                break
            p *= 2
        if flag:
            return "Корректен"
        else:
            return "Некорректен"
    else:
        return "Корректен"


print(check_pin('7-101-4'))