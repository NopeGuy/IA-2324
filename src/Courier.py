class Courier:
    def __init__(self, name, transport, orders=None):
        self.name = name
        self.transport = transport
        self._deliveries = []
        if orders is not None:
            self._deliveries.extend(orders)

    def add_delivery(self, order):
        self._deliveries.append(order)

    def get_deliveries(self):
        return self._deliveries

    def verifyWeight(self, order_weight):
        if self.transport == "Bicycle":
            return order_weight <= 5
        elif self.transport == "Moto":
            return order_weight <= 20
        elif self.transport == "Car":
            return order_weight <= 100
        else:
            return False
        
    def average_speed(self):
        if self.transport == "Bicycle":
            return 10
        elif self.transport == "Moto":
            return 35
        elif self.transport == "Car":
            return 50
        else:
            return 0
        
    def max_capacity(self):
        if self.transport == "Bicycle":
            return 5
        elif self.transport == "Moto":
            return 20
        elif self.transport == "Car":
            return 100
        else:
            return 0
        
    def verifyTime(self, path_cost, order_processing_time, weight):
        if self.transport == "Bicycle":
            max_time = path_cost / (self.average_speed() - (0.6*weight))* 60
            return max_time <= order_processing_time
        elif self.transport == "Moto":
            max_time = path_cost / (self.average_speed() - (0.5*weight))* 60
            return max_time <= order_processing_time
        elif self.transport == "Car":
            max_time = path_cost / (self.average_speed() - (0.1*weight))* 60
            return max_time <= order_processing_time