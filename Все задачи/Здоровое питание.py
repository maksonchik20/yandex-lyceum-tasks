def diet(s):
    global food
    args = s.split(', ')
    gr = len(args) // 2 + 1 if len(args) % 2 else len(args) // 2
    cnt = 0
    for el in args:
        if el not in food['диетическое']:
            cnt += 1
        if cnt >= gr:
            return 'Не ешь столько, По!'
    return 'Так держать, Воин Дракона!'

food = {'диетическое' : ["печенье", "чай", "сахар", "фрукты", "мед"]}

print(diet("печенье, чай, сахар, фрукты, мед"))