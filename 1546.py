class Tree:
    def __init__(self, ages):
        self.ages = ages

    def grow(self, years):
        self.ages += years

    def showAge(self):
        print("Tree ages:{}".format(self.ages))


while (1):
    a, b = [int(x) for x in input().split()]
    if a == 0 and b == 0:
        break
    tree = Tree(a)
    tree.grow(b)
    tree.showAge()
