class Bank:
    def __init__(self, name: str, address: str):
        self._name = name
        self._address = address

    @property
    def name(self):
        return self._name

    @property
    def address(self):
        return self._address
