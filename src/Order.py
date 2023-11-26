class Order:
    def __init__(self, client_name, weight, volume, processing_time, starting_node, last_node):
        self.client_name = client_name
        self.weight = weight
        self.volume = volume
        self.processing_time = processing_time
        self.starting_node = starting_node
        self.last_node = last_node