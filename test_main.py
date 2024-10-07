from unittest import TestCase
from main import *

DELTA = 10 ** -6


class TestPoint(TestCase):
    def test_distance(self):
        p = Point(1, 2)
        self.assertAlmostEqual(p.distance(2, 3), 1.414213, delta=DELTA)
        self.assertAlmostEqual(p.distance(-2, -3), 5.830951, delta=DELTA)


class Test(TestCase):
    def test_distance_between_points(self):
        p1 = Point(1, 2)
        p2 = Point(2, 3)
        p3 = Point(-2, -3)
        self.assertAlmostEqual(distance_between_points(p1, p2), 1.414213, delta=DELTA)
        self.assertAlmostEqual(distance_between_points(p1, p3), 5.830951, delta=DELTA)


class TestLine(TestCase):
    def test_length(self):
        l1 = Line(1, 2, 2, 3)
        self.assertAlmostEqual(l1.length(), 1.414213, delta=DELTA)


class TestCircle(TestCase):
    def test_area(self):
        c1 = Circle(10, 10, 5)
        c2 = Circle(5, 5, -5)
        c3 = Circle(5, 5, 0)
        self.assertAlmostEqual(c1.area(), 78.539816, delta=DELTA)
        self.assertAlmostEqual(c2.area(), 78.539816, delta=DELTA)
        self.assertAlmostEqual(c3.area(), 0, delta=DELTA)

    def test_circumference(self):
        c1 = Circle(10, 10, 5)
        c2 = Circle(10, 10, 0)
        self.assertAlmostEqual(c1.circumference(), 31.415926, delta=DELTA)
        self.assertAlmostEqual(c2.circumference(), 0.0, delta=DELTA)

    def test_distance(self):
        c1 = Circle(10, 10, 5)
        p1 = Point(5, 5)
        self.assertAlmostEqual(c1.distance(p1), 7.071067, delta=DELTA)

    def test_distance_between_centers(self):
        c1 = Circle(10, 10, 5)
        c2 = Circle(5, 5, 10)
        self.assertAlmostEqual(c1.distance_between_centers(c2), 7.071067, delta=DELTA)

    def test_is_intersecting(self):
        c1 = Circle(10, 10, 5)
        c2 = Circle(5, 5, 10)
        c3 = Circle(25, 25, 2)
        self.assertEqual(c1.is_intersecting(c2), True)
        self.assertEqual(c1.is_intersecting(c3), False)

    def test_area_of_intersection(self):
        c1 = Circle(10, 10, 5)
        c2 = Circle(25, 25, 5)
        self.assertAlmostEqual(c1.area_of_intersection(c2), 0.0, delta=DELTA)

        c3 = Circle(10, 10, 3)
        self.assertAlmostEqual(c1.area_of_intersection(c3), 28.0, delta=DELTA)

        c4 = Circle(10, 10, 7)
        self.assertAlmostEqual(c1.area_of_intersection(c4), 78.0, delta=DELTA)

        c5 = Circle(12, 12, 4)
        self.assertAlmostEqual(c1.area_of_intersection(c5), 37.0, delta=DELTA)


class TestRectangle(TestCase):
    def test_area(self):
        r = Rectangle(2, 2, 5, 5)
        self.assertAlmostEqual(r.area(), 9.0, delta=DELTA)

        r = Rectangle(-2, 2, 5, -5)
        self.assertAlmostEqual(r.area(), 49.0, delta=DELTA)

    def test_perimeter(self):
        r = Rectangle(2, 2, 5, 5)
        self.assertAlmostEqual(r.perimeter(), 12, delta=DELTA)

        r = Rectangle(-2, 2, 5, -5)
        self.assertAlmostEqual(r.perimeter(), 28, delta=DELTA)

    def test_distance_between_centers(self):
        r1 = Rectangle(2, 2, 5, 5)
        r2 = Rectangle(-2, 2, 5, -5)
        self.assertAlmostEqual(r1.distance_between_centers(r2), 5.385164, delta=DELTA)

    def test_is_intersecting(self):
        r1 = Rectangle(5, 5, 8, 3)
        r2 = Rectangle(-2, -2, -5, -5)
        self.assertEqual(r1.is_intersecting(r2), False)

        r3 = Rectangle(7, 7, 10, 10)
        self.assertEqual(r1.is_intersecting(r3), False)

        r4 = Rectangle(5, 4, 7, 2)
        self.assertEqual(r1.is_intersecting(r4), True)

    def test_intersection_area(self):
        r1 = Rectangle(5, 5, 8, 3)
        r2 = Rectangle(5, 4, 7, 2)
        # self.assertAlmostEqual(r1.intersection_area(r2), 10, delta=DELTA)

        r3 = Rectangle(10, 10, 13, 8)
        # self.assertAlmostEqual(r1.intersection_area(r3), 0, delta=DELTA)


class TestCuboid(TestCase):
    def test_volume(self):
        cube = Cuboid(5, 3, 3, 8, 0, 0)
        self.assertAlmostEqual(cube.volume(), 27, delta=DELTA)

    def test_surface_area(self):
        cube = Cuboid(5, 3, 3, 8, 0, 0)
        self.assertAlmostEqual(cube.surface_area(), 54, delta=DELTA)
