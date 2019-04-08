class Cuboid:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def length_set(self, length):
        self.length = length

    def width_set(self, width):
        self.width = width

    def height_set(self, height):
        self.height = height

    def getBottomArea(self):
        return self.length * self.width

    def getVolume(self):
        return self.length * self.width * self.height


l, w, h = [int(x) for x in input().split()]
cuboid = Cuboid(l, w, h)
print(cuboid.getBottomArea())
print(cuboid.getVolume())
