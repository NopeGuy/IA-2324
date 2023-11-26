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
