num = int(input())
result = 0
for i in range(1, num + 1):
    step = 0
    for j in range(1, i + 1):
        if i % 2 == 0:
            if j % 2 == 0:
                step += j
        else:
            if j % 2 != 0:
                step += j
    print(step)
    result += i ** step
print(result)