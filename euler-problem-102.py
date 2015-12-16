__author__ = 'sdenisenko'
import math
import unittest

class Point():
    def __init__(self, x=0, y=0):
        self.X = int(x)
        self.Y = int(y)

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

    def __str__(self):
        return "Triangle(%s; %s; %s)" % (self.point_1, self.point_2, self.point_3)


class UnitTestsTriangles(unittest.TestCase):
    def test_point_string(self):
        p = Point(0, 1)
        self.assertEqual(p.__str__(), "Point(0,1)")

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

    def test_parce_line_of_file(self):
        str = "-340,495,-153,-910,835,-947"
        array = str.split(",")
        self.assertEqual(array.__len__(), 6)


def parseInputData():
    count = 0
    count_triangles = 0
    triangles = []
    with open("input_data\\p102_triangles.txt", "r") as f:
        for line in f:
            coordinates = line.split(",")
            point_1 = Point(coordinates[0], coordinates[1])
            point_2 = Point(coordinates[2], coordinates[3])
            point_3 = Point(coordinates[4], coordinates[5])
            tr = Triangle(point_1, point_2, point_3)

            if tr.isContainsPoint(Point(0, 0)):
                triangles.append(tr)
                count += 1
            count_triangles +=1
    print triangles[0]
    print count_triangles
    print count

if __name__ == '__main__':
    unittest.main()

parseInputData()