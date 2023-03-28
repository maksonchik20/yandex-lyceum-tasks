d, s = int(input()), int(input())
x = 0
v = 0
def check_zam(now_v, now_x, to_x):
    while now_x < to_x and now_v > 1:
        now_v -= 1
        now_x += now_v
    if now_v > s:
        return 0
    return 1
# print(check_zam(2, 6, 5))
# s = 0
while x < d:
    if x+v+1 <= d and v+1<=s and check_zam(v, x + v + 1, d):
        v += 1
        x += v
    else:
        if check_zam(v, x, d):
            continue
        else:
            v -= 1
            x += v
    print(v, x)
    s += 1
print(s)
