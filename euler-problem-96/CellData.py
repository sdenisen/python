import unittest

__author__ = 'Sergey'


class CellData(object):
    IN = "IN"
    UNKNOWN = "UNKNOWN"
    SOLVED = "SOLVED"

    def __init__(self, value=None):
        self._value = value if value else 0
        self._state = self.UNKNOWN if self._value == 0 else self.IN
        self._suggests = [1, 2, 3, 4, 5, 6, 7, 8, 9] if self._state  == self.UNKNOWN else []

    @property
    def value(self):
        pass

    @value.getter
    def value(self):
        return self._value

    @property
    def state(self):
        pass

    @state.getter
    def state(self):
        return self._state

    @property
    def suggests(self):
        return self._suggests

    @suggests.setter
    def suggests(self, value):
        self._suggests = value

    @property
    def is_solved(self):
        return self._state != self.UNKNOWN

    def mark_solved(self):
        if len(self._suggests) == 1:
            self._state = CellData.SOLVED
            self._value = self._suggests[0]
            return True

        return False


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def testEmptyConstructor(self):
        c = CellData()
        self.assertEqual(c.state, CellData.UNKNOWN, "wrong state attribute")
        self.assertEqual(c.value, 0, "wrong default value")
        self.assertListEqual(c.suggests, [1, 2, 3, 4, 5, 6, 7, 8, 9], "wrong suggested value array")

        c = CellData(10)
        self.assertEqual(c.state, CellData.IN, "wrong state attribute")
        self.assertEqual(c.value, 10, "wrong default value")
        self.assertListEqual(c.suggests, [], "wrong suggested value array")
        self.assertTrue(c.is_solved, "incorrect return value")

    def testMarkSolvedOneElement(self):
        c = CellData(0)
        c.suggests = [4]
        self.assertFalse(c.is_solved, "incorrect return value")
        self.assertTrue(c.mark_solved(), "incorrect return value")
        self.assertTrue(c.is_solved, "incorrect return value")
        self.assertEqual(c.state, CellData.SOLVED, "incorrect value")

    def testMarkSolvedSeveralElements(self):
        c = CellData(0)
        c.suggests = [4, 5]
        self.assertFalse(c.mark_solved(), "incorrect return value")
        self.assertEqual(c.state, CellData.UNKNOWN, "incorrect value")
        self.assertFalse(c.is_solved, "incorrect return value")
