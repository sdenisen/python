__author__ = 'Sergey'

class CellData:
    IN = "IN"
    UNKNOWN = "UNKNOWN"
    SOLVED = "SOLVED"

    def __init__(self, value=None, state=None, suggests=None):
        self._value = value if value else 0
        self._state = state if state else self.UNKNOWN
        self._suggests = suggests if suggests else [1,2,3,4,5,6,7,8,9]

    @property
    def value(self):
        return self._value

    @property
    def state(self):
        return self._state

    @property
    def suggests(self):
        return self._suggests

    @suggests.setter
    def suggests(self, value):
        self._suggests = value


