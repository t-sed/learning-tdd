class Dollar:
    def __init__(self, amount: int):
        self.amount = amount

    def times(self, times: int):
        self.amount *= times
