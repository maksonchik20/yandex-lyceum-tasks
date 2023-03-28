games = {}

for _ in range(int(input())):
    games[input().upper()] = 0

nums = []
while (num := input()) != '':
    nums.append(num)

for game, value in games.items():
    _min = 10 ** 9
    for num in nums:
        flag = True
        for len_simv_game in str(len(game)):
            if len_simv_game not in num:
                flag = False
        if flag:
            _min = min(int(num), _min)
    if _min != 10 ** 9:
        games[game] = _min
        
print(games)
