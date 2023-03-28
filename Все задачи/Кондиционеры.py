
def main():
    n = int(input())
    data = list(map(int, input().split()))
    r = int(input())
    condition = [list(map(int, input().split())) for _ in range(r)]

    _sum = 0
    for i in data:
        _min = 1_000_000
        for j in condition:
            if j[0] >= i:
                _min = min(_min, j[1])
        _sum += _min
    return _sum

print(main())

# from math import factorial as ft

# m, n = map(int, input().split())

# one = (ft(m) / ft(m - 1)) * (ft(n) / (ft(3) * ft(n - 3)))
# two = (ft(m) / (ft(m - 2) * ft(2))) * (ft(n) / (ft(2) * ft(n - 2)))
# three = (ft(m) / (ft(m - 3) * ft(3))) * (ft(n) / (ft(n - 1)))
# print(int(one + two + three))


