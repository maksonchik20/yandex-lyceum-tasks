from pprint import pprint
class SeaMap:
    def __init__(self):
        self.place = [['.' for j in range(10)] for i in range(10)]
    
    def shoot(self, row, col, result):
        if result == 'miss':
            self.place[row][col] = '*'
        elif result == 'hit':
            self.place[row][col] = 'x'
        elif result == 'sink':
            self.place[row][col] = 'x'
            if row > 0:
                if col > 0:
                    self.place[row - 1][col - 1] = '*'
                elif col < 9:
                    self.place[row - 1][col + 1] = '*'
            elif row < 9:
                if col > 0:
                    self.place[row + 1][col - 1] = '*'
                elif col < 9:
                    self.place[row + 1][col + 1] = '*'
            self._rec(row, col)
                
    def _rec(self, row, col):
        result = []
        flag = False
        for new_col in range(col + 1, 10):
            if self.place[row][new_col] == 'x':
                self.place[row + 1][new_col] = '*'
                self.place[row - 1][new_col] = '*'
            if new_col < 9:
                if self.place[row][new_col + 1] != 'x':
                    self.place[row][new_col + 1] = '*'
                    flag = True
                    if row > 0:
                        self.place[row - 1][new_col + 1] = '*'
                    if row < 9:
                        self.place[row + 1][new_col + 1] = '*'
            if flag:
                break
        for new_col in range(col - 1, -1, -1):
            print(new_col)
            if new_col > 0:
                if self.place[row][new_col - 1] != 'x' and self.place[row][new_col] == 'x':
                    self.place[row][new_col - 1] = '*'
                    flag = True
                    if row > 0:
                        self.place[row - 1][new_col - 1] = '*'
                    if row < 9:
                        self.place[row + 1][new_col - 1] = '*'
            if flag:
                break
            if self.place[row][new_col] == 'x':
                self.place[row + 1][new_col] = '*'
                self.place[row - 1][new_col] = '*'
                if row > 0:
                    self.place[row - 1][new_col - 1] = '*'
                    self.place[row + 1][new_col - 1] = '*'
        return result
    def cell(self, row, col):
        return self.place[row][col]
        
sm = SeaMap()
# sm.shoot(0, 0, 'sink')
sm.shoot(6, 7, 'hit')
# sm.shoot(6, 8, 'hit')
sm.shoot(6, 6, 'hit')
sm.shoot(6, 5, 'sink')

for row in range(10):
    for col in range(10):
        print(sm.cell(row, col), end='')
    print()