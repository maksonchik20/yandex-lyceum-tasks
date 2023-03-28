class Table:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.array = [[0 for _ in range(cols)] for _ in range(rows)]
    
    def get_value(self, row: int, col: int):
        if self.rows > row >= 0 and self.cols > col >= 0:
            return self.array[row][col]
        return None
    
    def set_value(self, row: int, col: int, value: int):
        self.array[row][col] = value
    
    def n_rows(self):
        return self.rows
    
    def n_cols(self):
        return self.cols
    
    def add_row(self, row: int):
        self.array = self.array[:row] + [[0 for _ in range(self.cols)]] + self.array[row:]
        self.rows += 1
    
    def delete_row(self, row: int):
        self.array = self.array[:row] + self.array[row + 1:]
        self.rows -= 1
    
    def add_col(self, col: int):
        for row in range(self.rows):
            self.array[row] = self.array[row][:col] + [0] + self.array[row][col:]
        self.cols += 1
    
    def delete_col(self, col: int):
        for row in range(self.rows):
            self.array[row] = self.array[row][:col] + self.array[row][col + 1:]
        self.cols -= 1
