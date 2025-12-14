from bank import Bank


class BankBranch(Bank):
    def __init__(self, name: str, address: str, number: int):
        super().__init__(name, address)
        self._number = number

    @property
    def number(self):
        return self._number
