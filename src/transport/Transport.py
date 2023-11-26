class Transport:
    def __init__(self, maxCapacity, avgSpeed):
        self.maxCapacity = maxCapacity
        self.avgSpeed = avgSpeed

    def verifyWeight(self, orderWeight):
        return orderWeight <= self.maxCapacity

    def calculateDeliveryTime(self, distanceKM):
        return distanceKM / self.avgSpeed


class Bicycle(Transport):
    def __init__(self, maxCapacity=5, avgSpeed=10):
        super().__init__(maxCapacity, avgSpeed)


class Car(Transport):
    def __init__(self, maxCapacity=100, avgSpeed=50):
        super().__init__(maxCapacity, avgSpeed)


class Moto(Transport):
    def __init__(self, maxCapacity=20, avgSpeed=35):
        super().__init__(maxCapacity, avgSpeed)
