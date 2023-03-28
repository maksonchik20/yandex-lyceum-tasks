str1, str2 = input(), input()
print('ВЕРНО' if str2[0] == (str1[-2] if str1[-1] == 'ь' else str1[-1]) else 'НЕВЕРНО')
