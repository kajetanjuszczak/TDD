class Dollar:
    def __init__(self, n):
        self.amount = n

    def multiply(self, multiplier):
        return Dollar(self.amount * multiplier)