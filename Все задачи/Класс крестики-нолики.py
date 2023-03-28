class TicTacToeBoard:
    def __init__(self):
        self.winner = None
        self.place = [['-' for _ in range(3)] for _ in range(3)]