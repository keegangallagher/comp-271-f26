from math import ceil

class Array271:

    def __init__(self, capacity: int = 2, resize_factor: float = 0.25):
        self._capacity: int = capacity
        self._resize_factor: float = resize_factor
        self._occupancy: int = 0
        self._items: list = [None] * capacity

    def get_capacity(self):
        return self._capacity
    def get_resize_factor(self):
        return self._resize_factor
    def get_occupancy(self):
        return self._occupancy
    def get_items(self):
        return self._items

    def get_item(self, i):
        return self._items[i]


    def add(self, value: str):
        if self._occupancy == self._capacity:
            self._resize()
        self._items[self._occupancy] = value
        self._occupancy += 1

    def _resize(self):
        growth = ceil(self._capacity*(1+self._resize_factor))
        temp = [None] * growth
        for i in range(self._capacity):
            temp[i] = self._items[i]
        self._items = temp
        self._capacity = growth

