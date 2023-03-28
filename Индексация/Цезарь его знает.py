step = int(input())
word = input()
alphabet_lower = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
alphaber_upper = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
result = ""
for i in word:
    flag = False
    if i.isalpha():
        if i in alphabet_lower:
            flag = True
        number = ord(i) + step % 32
        if number > 1103:
            number -= 32
        if flag:
            result += chr(number).lower()
        else:
            result += chr(number).upper()
    else:
        result += i
print(result)
