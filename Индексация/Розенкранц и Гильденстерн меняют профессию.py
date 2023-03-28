_str = input()
right = 1
_max = 0
for left in range(len(_str)):
    if 'р' in _str[left:right + 1]:
        continue
    if _str[left:right] == 'о' * (right - left):
        while 'р' not in _str[left:right] and right <= len(_str):
            _max = max(_max, len(_str[left:right]))
            right += 1
print(_max)
            

