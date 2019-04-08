class Vehicle:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Car(Vehicle):
    def __init__(self, name, color, passenger):
        super().__init__(name, color)
        self.passenger = passenger

    def out(self):
        print('Car\'s name:{}'.format(self.name))
        print('Car\'s color:{}'.format(self.color))
        print('Car\'s passengerNumber:{}'.format(self.passenger))


class Truck(Vehicle):
    def __init__(self, name, color, carrying):
        super().__init__(name, color)
        self.carrying = carrying

    def out(self):
        print('Truck\'s name:{}'.format(self.name))
        print('Truck\'s color:{}'.format(self.color))
        print('Truck\'s carryingCapacity:{:.1f}'.format(float(self.carrying)))


a, b, c = input().split()
car = Car(a, b, c)
a, b, c = input().split()
truck = Truck(a, b, c)
car.out()
truck.out()
