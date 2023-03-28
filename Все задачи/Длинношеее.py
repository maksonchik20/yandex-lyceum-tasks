def print_long_words(text):
    glas = ['а', 'о', 'э', 'и', 'у', 'ы', 'е', 'ё', 'ю', 'я', 'a', 'e', 'i', 'o', 'u', 'y']
    text = " " + text.lower() + " "
    # если мы считаем первое и последнее слово, что оно ограничено правильно, то так
    # если не считаем, то просто text = text
    # left = 1
    left = 1
    cnt = 0
    right = 0
    for i in range(len(text)):
        if not text[i].isalpha():
            if cnt >= 4:
                print(text[right + 1:left - 1].lower())
            right = i
            left += 1
            cnt = 0
        else:
            if text[i] in glas:
                cnt += 1
            left += 1
print_long_words('Как и в прочих заданиях этого урока, в вашем решении функция должна быть определена, но не должна вызываться.')
