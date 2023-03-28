def tic_tac_toe(f):
    for i in range(3):
        if f[i][0] == f[i][1] == f[i][2]:
            print(f[i][0] + ' win')
            return
    for i in range(3):
        if f[0][i] == f[1][i] == f[2][i]:
            print(f[0][i] + ' win')
            return
    if f[0][0] == f[1][1] == f[2][2]:
        print(f[0][0] + ' win')
    elif f[0][2] == f[1][1] == f[2][0]:
        print(f[0][2] + ' win')
    else:
        print('draw')


data = """0 - 0
0 - x
0 0 -"""

field = [line.split() for line in data.split('\n')]
tic_tac_toe(field)