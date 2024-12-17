class ElementNazmetdinov:
    def __init__(self, name, symbol, number):
        self._name = name
        self._symbol = symbol
        self._number = number

    @property
    def name(self):
        return self._name

    @property
    def symbol(self):
        return self._symbol

    @property
    def number(self):
        return self._number

    def dump(self):
        print(f"Name: {self.name}, Symbol: {self.symbol}, Number: {self.number}")

element = ElementNazmetdinov("Кремний", "Si", 14)
element.dump()