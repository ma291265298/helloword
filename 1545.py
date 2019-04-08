import math


class GeometricObject:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled


class Triangle(GeometricObject):

    def __init__(self, color, filled, side1=1.0, side2=1.0, side3=1.0):
        super().__init__(color, filled)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def getArea(self):
        p = (self.side3 + self.side2 + self.side1) / 2
        return math.sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3))

    def getPerimeter(self):
        return self.side3 + self.side2 + self.side1

    def run(self):
        print("Triangle: side1={} side2={} side3={} color={} filled={}"
              .format(self.side1, self.side2, self.side3, self.color, self.filled))
        print("Area={:.2f}".format(self.getArea()))
        print("Perimeter={:.2f}".format(self.getPerimeter()))


s1, s2, s3, c, f = input().split()
triangle = Triangle(c, f, float(s1), float(s2), float(s3))
triangle.run()
