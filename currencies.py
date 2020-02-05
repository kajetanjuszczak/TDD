class Dollar:
    def __init__(self, n):
        self.amount = n

    def __eq__(self, other):
        if not isinstance(other, Dollar):
            return NotImplemented
        return self.amount == other.amount

    def multiply(self, multiplier):
        return Dollar(self.amount * multiplier)
