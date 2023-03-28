pay_horse = []


def do_bet(horse, pay):
    global pay_horse
    if horse in pay_horse or pay == 0 or horse > 10 or horse < 1:
        print('Что-то пошло не так, попробуйте еще раз')
    else:
        print(f"Ваша ставка в размере {pay} на лошадь {horse} принята")