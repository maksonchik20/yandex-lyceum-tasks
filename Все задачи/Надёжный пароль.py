def password_level(password):
    if len(password) < 6:
        return 'Недопустимый пароль'
    
    upp_let = False
    low_let = False
    dig_let = False
    for let in password:
        if let.islower():
            low_let = True
        if let.isupper():
            upp_let = True
        if let.isdigit():
            dig_let = True
    if dig_let and not upp_let and not low_let or not dig_let and upp_let and not low_let:
        return "Ненадежный пароль"
    elif not dig_let and not upp_let and low_let:
        return "Ненадежный пароль"
    elif upp_let and low_let and dig_let:
        return "Надежный пароль"
    else:
        return "Слабый пароль"

print(password_level("qwerty"))
    