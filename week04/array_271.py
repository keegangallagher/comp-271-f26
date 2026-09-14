# Week 04 version 

from math import ceil

class Array271: 

    def __init__(self, capacity: int = 2, resize_factor: float = 0.25):
        self._capacity: int = capacity
        self._resize_factor: float = resize_factor
        self._occupancy: int = 0
        self._items: list = [None] * capacity

    def __str__(self) -> str:
        """Return a human-readable summary: capacity, occupancy, and the
        occupied slots only (not the trailing Nones)."""
        occupied = self._items[: self._occupancy]
        return (
            f"Array271(capacity={self._capacity}, "
            f"occupancy={self._occupancy}, items={occupied})"
        )

    # ------------------------------------------------------------------
    # Accessors -- the only sanctioned way to read a private attribute
    # from outside the class.
    # ------------------------------------------------------------------

    def get_capacity(self) -> int:
        return self._capacity

    def get_resize_factor(self) -> float:
        return self._resize_factor

    def get_occupancy(self) -> int:
        return self._occupancy

    def get_items(self) -> list:
        return self._items

    def get_item(self, i: int):
        item = None
        if 0 <= i < self._occupancy:
            item = self._items[i]
        return item

    # ------------------------------------------------------------------
    # Mutators
    # ------------------------------------------------------------------

    def add(self, value: str):
        if self.__occupancy == self.__capacity:
            self.__resize()
        self.__items[self.__occupancy] = value
        self.__occupancy += 1

    def __resize(self):
        growth = ceil(self.__capacity*(1+self.__resize_factor))
        temp = [None] * growth
        for i in range(self.__capacity):
            temp[i] = self.__items[i]
        self.__items = temp
        self.__capacity = growth


    def remove(self, i):
        success = i >= 0 and i < self.__occupancy
        if success:
            self.__items[i] = None
        return success
