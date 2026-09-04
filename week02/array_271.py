class Array271:

    def __init__(self, capacity:int = 2, resize_factor:float = 0.25):
        self.capacity: int = capacity
        self.resize_factor: float = resize_factor
        self.occupancy: int = 0
