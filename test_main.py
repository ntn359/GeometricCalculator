from unittest import TestCase
from main import *


class TestPoint(TestCase):
    def test_distance(self):
        p = Point(1, 2)
        self.assertAlmostEqual(p.distance(2, 3), 1.414213, delta=10 ** -6)
        self.assertAlmostEqual(p.distance(-2, -3), 5.830951, delta=10 ** -6)


class Test(TestCase):
    def test_distance_between_points(self):
        p1 = Point(1, 2)
        p2 = Point(2, 3)
        p3 = Point(-2, -3)
        self.assertAlmostEqual(distance_between_points(p1, p2), 1.414213, delta=10 ** -6)
        self.assertAlmostEqual(distance_between_points(p1, p3), 5.830951, delta=10 ** -6)


class TestLine(TestCase):
    def test_length(self):
        l1 = Line(1, 2, 2, 3)
        self.assertAlmostEqual(l1.length(), 1.414213, delta=10 ** -6)


class TestCircle(TestCase):
    def test_area(self):
        c1 = Circle(10,10, 5)
        c2 = Circle(5,5,-5)
        c3 = Circle(5, 5, 0)
        self.assertAlmostEqual(c1.area(), 78.539816, delta=10**-6)
        self.assertAlmostEqual(c2.area(), 78.539816, delta=10 ** -6)
        self.assertAlmostEqual(c3.area(), 0, delta=10 ** -6)
