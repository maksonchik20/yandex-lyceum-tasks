num = int(input())

for i in range(2, num):
    flag = True
    for j in range(2, (i // 2) + 1):
        if i % j == 0:
            flag = False
            break
    if flag:
        print(i)
        
        