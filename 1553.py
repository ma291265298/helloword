class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def getVolume(self):
        return 3.14 * self.radius ** 2 * self.height


r, h = [int(x) for x in input().split()]
cylinder = Cylinder(r, h)
print('{:.2f}'.format(cylinder.getVolume()))
