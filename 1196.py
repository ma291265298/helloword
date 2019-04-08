class Cube:
    __edge = 0
    __volume = 0
    __area = 0

    def __init__(self, edge):
        self.__edge = edge
        self.calVolume()
        self.calArea()

    def calVolume(self):
        self.__volume = int(self.__edge ** 3*100+0.5)/100
        return self.__volume

    def calArea(self):
        self.__area = int(6 * self.__edge ** 2*100+0.5)/100
        return self.__area

    def display(self):
        print("obj1 Volume:{:.2f}; Area:{:.2f} ".format(self.__volume, self.__area))


n = int(input())
for i in range(n):
    x = float(input())
    cube = Cube(x)
    cube.display()
