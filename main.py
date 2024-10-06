import sys
import numpy as np

class Point:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def distance(self, x,y):
        return np.sqrt(np.square(x - self.x) + np.square(y - self.y))

def distance_between_points(p1, p2) -> object:
    return np.sqrt(np.square(p1.x - p2.x) + np.square(p1.y - p2.y))


class Line:
    def __init__(self, x1,y1,x2,y2):
        self.p1 = Point(x1,y1)
        self.p2 = Point(x2,y2)

    def length(self):
        return distance_between_points(self.p1,self.p2)

class Circle:
    def __init__(self, x, y, rad):
        if rad<0:
            print("Radius of circle cannot be negative\nTaking abs value of input")
        self.center = Point(x,y)
        self.radius = np.abs(rad)

    def area(self):
        if self.radius>0:
            return np.pi * self.radius * self.radius
        else:
            print("Cannot find area of invalid circle")
            return 0

    def circumference(self):
        return 2* np.pi *self.radius

    def distance(self, p):
        return np.sqrt(np.square(p.x - self.center.x) + np.square(p.y-self.center.y))

    def distance_between_centers(self, c):
        return np.sqrt(np.square(c.center.x - self.center.x) + np.square(c.center.y - self.center.y))

    def is_intersecting(self, c):
        d = self.center.distance(c.x, c.y)
        if d <= self.radius + c.radius: # Non-intersecting circle
            return True
        return False

    def area_of_intersection(self, x2, y2, r2):
        x1 = self.center.x
        y1 = self.center.y
        r1 = self.radius
        d = self.center.distance(x2, y2)

        if d > r1 + r2: # Non-intersecting circle
            ans = 0

        elif d <= (r1 - r2) and r1 >= r2: # second circle inside first
            ans = np.floor(np.pi * r2 * r2)

        elif d <= (r2 - r1) and r2 >= r1: # first circle inside second
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
        self.tl = Point(x1, y1)
        self.br = Point(x2, y2)

    def area(self):
        return np.abs(self.tl.x - self.br.x) * np.abs(self.tl.y - self.br.y)

    def perimeter(self):
        return 2 * (np.abs(self.tl.x - self.br.x) + np.abs(self.tl.y - self.br.y))

    def is_intersecting(self, rect):
        # If one rectangle is to the left of the other
        if self.tl.x > rect.br.x or rect.tl.x > self.br.x:
            return False

        # If one rectangle is above the other
        if self.br.y > rect.tl.y or rect.br.y > self.tl.y:
            return False

        return True

    def intersection_area(self, rect):
        # Area of 1st Rectangle
        l1 = Point(self.tl.x, self.tl.y)
        r1 = Point(self.br.x, self.br.y)
        l2 = Point(rect.tl.x, rect.tl.y)
        r2 = Point(rect.br.x, rect.br.y)

        area1 = abs(l1.x - r1.x) * abs(l1.y - r1.y)

        # Area of 2nd Rectangle
        area2 = abs(l2.x - r2.x) * abs(l2.y - r2.y)

        x_dist = (min(r1.x, r2.x) -
                  max(l1.x, l2.x))

        y_dist = (min(r1.y, r2.y) -
                  max(l1.y, l2.y))
        area_int = 0
        if x_dist > 0 and y_dist > 0:
            area_int = x_dist * y_dist

        return area1 + area2 - area_int


def __main__():
    print("hello")


