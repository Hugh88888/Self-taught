import math

class Apple:
    def __init__(self, color, weight, quantity, taste):
        self.color = color
        self.weight = weight
        self.quantity = quantity
        self.taste = taste


class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return self.r ** 2 * math.pi

a_c = Circle(4)
print(a_c.area())

class Triangle:
    def __init__(self, u, h):
        self.u = u
        self.h = h

    def area(self):
        return self.u * self.h / 2

u_h = Triangle(4, 4)
print(u_h.area())

class Hexagon:
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6

    def calculate_perimeter(self):
        return self.s1 + self.s2 + self.s3 + self.s4 + self.s5 + self.s6

s = Hexagon(2, 2, 2, 2, 2, 2)
print(s.calculate_perimeter())
