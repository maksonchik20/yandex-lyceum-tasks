class Selector:
    def __init__(self, array: list):
        self.array = array.copy()
    
    def get_odds(self):
        res = []
        for el in self.array:
            if el % 2 != 0:
                res.append(el)
        return res
    
    def get_evens(self):
        res = []
        for el in self.array:
            if el % 2 == 0:
                res.append(el)
        return res