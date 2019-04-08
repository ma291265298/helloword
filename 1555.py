class Circle:
    __radius = 1
    __x = 0
    __y = 0

    def __init__(self, x, y, radius):
        self.__radius = radius
        self.__x = x
        self.__y = y

    def calDiameter(self):
        print('Diameter={}'.format(2 * self.__radius))

    def calArea(self):
        print('Area={:.1f}'.format(3.14 * self.__radius ** 2))

    def calPerimeter(self):
        print('Perimeter={:.1f}'.format(2 * 3.14 * self.__radius))

    def output(self):
        print('Center=({},{}) and Radius={} '.format(self.__x, self.__y, self.__radius))


a, b, c = [int(x) for x in input().split()]
circle = Circle(a, b, c)
circle.output()
circle.calDiameter()
circle.calArea()
circle.calPerimeter()
