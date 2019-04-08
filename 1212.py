class Shape:
    def area(self):
        pass

    def vol(self):
        pass


class Cylinder(Shape):
    def __init__(self, r, h):
        self.r = r
        self.h = h

    def area(self):
        are = 3.14 * 2 * self.r * self.h + 3.14 * self.r ** 2*2
        return are

    def vol(self):
        vl = 3.14*self.r ** 2 * self.h
        return vl


class Ball(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        are = 4 * 3.14 * self.r ** 2
        return are

    def vol(self):
        vl = 4 * 3.14 * self.r ** 3 / 3
        return vl


class Cube(Shape):
    def __init__(self, a):
        self.a = a

    def area(self):
        are = 6 * self.a ** 2
        return are

    def vol(self):
        vl = self.a ** 3
        return vl


class Cuboid(Shape):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def area(self):
        are = 2 * (self.a * self.b + self.a * self.h + self.b * self.h)
        return are

    def vol(self):
        vl = self.a * self.b * self.h
        return vl


n = int(input())
for i in range(n):
    r, h = [float(x) for x in input().split()]
    cylinder = Cylinder(r, h)
    r = float(input())
    ball = Ball(r)
    r = float(input())
    cube = Cube(r)
    a, b, h = [float(x) for x in input().split()]
    cuboid = Cuboid(a, b, h)
    print('{:.2f} {:.2f}'.format(cylinder.area(), cylinder.vol()))
    print('{:.2f} {:.2f}'.format(ball.area(), ball.vol()))
    print('{:.2f} {:.2f}'.format(cube.area(), cube.vol()))
    print('{:.2f} {:.2f}'.format(cuboid.area(), cuboid.vol()))
