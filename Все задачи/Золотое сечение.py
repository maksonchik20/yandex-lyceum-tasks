def golden_ratio(num:int) -> float:
    f = fib(num + 1)
    print(f[-1] / f[-2])

def fib(i):
    f = [1, 1]
    for i in range(2, i):
        f.append(f[i - 2] + f[i - 1])
    return f

# print(fib(5))
# golden_ratio(2)