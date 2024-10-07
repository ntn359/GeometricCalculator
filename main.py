import numpy as np


class Point:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        """
        Point class constructor

        :param x: x-axis value of point
        :param y: y-axis value of point
        :param z: z-axis value of point
        :return: object
        """
        self.x = x
        self.y = y
        self.z = z

    def distance(self, x, y, z=0):
        """
         func to find distance between 2 points

         :param x: x-axis value of point
         :param y: y-axis value of point
         :param z: z-axis value of point
         :return: Euclidean distance
         """
        return np.sqrt(np.square(x - self.x) + np.square(y - self.y)+ np.square(z - self.z))


def distance_between_points(p1, p2) -> object:
    """
    func to find distance between 2 points

    :param p1: point 1 obj
    :param p2: point 2 obj
    :return: Euclidean distance
    """
    return np.sqrt(np.square(p1.x - p2.x) + np.square(p1.y - p2.y) + np.square(p1.z - p2.z))


class Line:
    def __init__(self, x1, y1, x2, y2):
        """
         Line class constructor

         :param x1: x-axis value of point1
         :param y1: y-axis value of point1
         :param x2: x-axis value of point2
         :param y2: y-axis value of point2
         :return: line obj
         """
        self.p1 = Point(x1, y1)
        self.p2 = Point(x2, y2)

    def length(self):
        """
        func to find length of the line

        :return: length of the line
        """
        return distance_between_points(self.p1, self.p2)


class Circle:
    def __init__(self, x, y, rad):
        """
        Circle class constructor
        :param x: x-axis value of center point
        :param y: y-axis value of center point
        :param rad: radius of the circle
        """
        if rad < 0:
            print("Radius of circle cannot be negative\nTaking abs value of input")
        self.center = Point(x, y)
        self.radius = np.abs(rad)

    def area(self):
        """
        func to find area of the circle
        :return: area of the circle
        """
        if self.radius > 0:
            return np.pi * self.radius * self.radius
        else:
            print("Cannot find area of invalid circle")
            return 0

    def circumference(self):
        """
        func to find circumference of the circle
        :return: circumference of the circle
        """
        return 2 * np.pi * self.radius

    def distance(self, p):
        """
        func to find distance between a point and center point of the circle
        :param p: point obj
        :return: Euclidean distance between point and center point
        """
        return np.sqrt(np.square(p.x - self.center.x) + np.square(p.y - self.center.y))

    def distance_between_centers(self, c):
        """
        func to find distance between centers of 2 circles
        :param c: second circle obj
        :return: Euclidean distance
        """
        return np.sqrt(np.square(c.center.x - self.center.x) + np.square(c.center.y - self.center.y))

    def is_intersecting(self, c):
        """
        func to check whether 2 circles are intersecting
        :param c: other circle
        :return: circles are intersecting or not
        """
        d = self.center.distance(c.center.x, c.center.y)
        if d <= self.radius + c.radius:  # Non-intersecting circle
            return True
        return False

    def area_of_intersection(self, c):
        """
        func to find area of intersection of 2 circles
        :param c: other circle
        :return: area of intersection of 2 circles
        """
        r1 = self.radius

        x2 = c.center.x
        y2 = c.center.y
        r2 = c.radius

        d = self.center.distance(x2, y2)

        if d > r1 + r2:  # Non-intersecting circle
            ans = 0.0

        elif d <= (r1 - r2) and r1 >= r2:  # second circle inside first
            ans = np.floor(np.pi * r2 * r2)

        elif d <= (r2 - r1) and r2 >= r1:  # first circle inside second
            ans = np.floor(np.pi * r1 * r1)

        else:
            alpha = np.acos(((r1 * r1) + (d * d) - (r2 * r2)) / (2 * r1 * d)) * 2
            beta = np.acos(((r2 * r2) + (d * d) - (r1 * r1)) / (2 * r2 * d)) * 2

            a1 = (0.5 * beta * r2 * r2) - (0.5 * r2 * r2 * np.sin(beta))
            a2 = (0.5 * alpha * r1 * r1) - (0.5 * r1 * r1 * np.sin(alpha))
            ans = np.floor(a1 + a2)

        return ans


class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        """
        Rectangle class constructor
        :param x1: x-axis value of top left point of rect
        :param y1: y-axis value of top left point of rect
        :param x2: x-axis value of bottom right point of rect
        :param y2: y-axis value of bottom right point of rect
        """
        self.tl = Point(x1, y1)
        self.br = Point(x2, y2)

    def area(self):
        """
        func to find area of rect
        :return: area of rect
        """
        return np.abs(self.tl.x - self.br.x) * np.abs(self.tl.y - self.br.y)

    def perimeter(self):
        """
        func to find perimeter of rect
        :return: perimeter of rect
        """
        return 2 * (np.abs(self.tl.x - self.br.x) + np.abs(self.tl.y - self.br.y))

    def distance_between_centers(self, rect):
        """
        func to find distance between center points of 2 rects
        :param rect: other rect
        :return: Euclidean distance between 2 center points
        """
        p1 = Point((self.tl.x + self.br.x) / 2, (self.tl.y + self.br.y) / 2)
        p2 = Point((rect.tl.x + rect.br.x) / 2, (rect.tl.y + rect.br.y) / 2)
        return distance_between_points(p1, p2)

    def is_intersecting(self, rect):
        """
        func to check whether rectangles are intersecting or not
        :param rect: other rect
        :return: whether rectangles are intersecting or not
        """
        # If one rectangle is to the left of the other
        if self.tl.x > rect.br.x or rect.tl.x > self.br.x:
            return False

        # If one rectangle is above the other
        if self.br.y > rect.tl.y or rect.br.y > self.tl.y:
            return False

        return True

    def intersection_area(self, rect):
        """
        func to find area of intersection of 2 rects
        :param rect: other rect
        :return: area of intersection of 2 rects
        """
        l1 = Point(self.tl.x, self.tl.y)
        r1 = Point(self.br.x, self.br.y)
        l2 = Point(rect.tl.x, rect.tl.y)
        r2 = Point(rect.br.x, rect.br.y)

        x1overlap = min(l1.x, l2.x)
        x2overlap = max(r1.x, r2.x)

        y1overlap = min(l1.y, l2.y)
        y2overlap = max(r1.y, r2.y)
        if x2overlap < x1overlap and y2overlap < y1overlap:
            return (x2overlap - x1overlap) * (y2overlap - y1overlap)
        else:
            return 0


class Cuboid:
    def __init__(self, x1, y1, z1, x2, y2, z2):
        """
        Cuboid class constructor
        :param x1: x-axis value of front top left point of cuboid
        :param y1: y-axis value of front top left point of cuboid
        :param z1: z-axis value of front top left point of cuboid
        :param x2: x-axis value of back bottom right point of cuboid
        :param y2: y-axis value of back bottom right point of cuboid
        :param z2: z-axis value of back bottom right point of cuboid
        """
        self.tl = Point(x1, y1, z1)
        self.br = Point(x2, y2, z2)
        self.length = np.abs(x1 - x2)
        self.breadth = np.abs(y1 - y2)
        self.depth = np.abs(z1 - z2)

    def volume(self):
        """
        func to find volume of cuboid
        :return: volume of cuboid
        """
        return self.length * self.breadth * self.depth

    def surface_area(self):
        """
        func to find surface area of cuboid
        :return: surface area of cuboid
        """
        return 2 * (self.length * self.breadth + self.breadth * self.depth + self.depth * self.length)
