height, width, simv = int(input()), int(input()), input()
print(width * simv)
for i in range(height - 2):
    print(simv + ' ' * (width - 2) + simv )
print(width * simv)