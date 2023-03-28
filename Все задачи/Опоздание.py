def get_line_time(time):
    h, m = map(int, time.split(':'))
    return h * 60 + m

def late(now, classes, bus):
    now_ln_time = get_line_time(now)
    cl_ln_time = get_line_time(classes)
    result = "Опоздание"
    for el in bus:
        if el >= 5:
            new_ln_time_bus = now_ln_time + el
            if new_ln_time_bus + 15 <= cl_ln_time:
                result = f"Выйти через {el - 5} минут"
    return result
    

print(late('12:00', '12:40', [0, 1, 4, 6, 25]))
print(late('9:20', '9:35', [4, 25, 30]))