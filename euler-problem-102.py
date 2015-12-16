__author__ = 'sdenisenko'
import math
import unittest

class Point():
    def __init__(self, x=0, y=0):
        self.X = x
        self.Y = y

    def __str__(self):
        return "Point(%s,%s)" % (self.X, self.Y)

    def distance(self, other):
        dx = self.X - other.X
        dy = self.Y - other.Y
        return math.sqrt(dx**2+dy**2)

class Triangle():
    def __init__(self, point_1, point_2, point_3):
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3

    def isContainsPoint(self, point):
        if (self.point_1.X - point.X)*(self.point_2.Y - self.point_1.Y) > (self.point_2.X - self.point_1.X)*(self.point_1.Y - point.Y) and \
            (self.point_2.X - point.X)*(self.point_3.Y - self.point_2.Y) > (self.point_3.X - self.point_2.X)*(self.point_2.Y - point.Y) and  \
            (self.point_3.X - point.X)*(self.point_1.Y - self.point_3.Y) > (self.point_1.X - self.point_3.X)*(self.point_3.Y - point.Y):
            return True
        return False


class UnitTestsTriangles(unittest.TestCase):
    def test_is_contains_point_success(self):
        A = Point(-340, 495)
        B = Point(-153, -910)
        C = Point(835, -947)
        triangle = Triangle(A, B, C)

        self.assertTrue(triangle.isContainsPoint(Point(0, 0)))
    def test_is_contains_point_UN_success(self):
        A = Point(-174, 41)
        B = Point(-421, -714)
        C = Point(574, -645)
        triangle = Triangle(A, B, C)

        self.assertFalse(triangle.isContainsPoint(Point(0, 0)))


def parseInputData():
    triangles = []
    with open():
        pass
    pass

if __name__ == '__main__':
    unittest.main()