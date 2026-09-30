from __future__ import annotations
from Station import *


class BetterTrainLine:

    def __init__(self, name: str):
        self.__name: str = name
        self.__head: Station = None
        self.__last: Station = None
        self.__size: int = 0

    def __str__(self):
        return f"Better Train Line name: {self.__name}"

    def add(self, new_station: Station):
        if self.__head == None:
            self.__head = new_station
        else:
            self.__last.set_next(new_station)
        self.__last = new_station
        self.__size += 1

    def find_middle_station(self) -> Station:
        slow: Station = self.__head
        fast: Station = self.__head
        while fast.has_next() and fast.get_next().has_next():
            slow = slow.get_next()
            fast = fast.get_next().get_next()
        return slow

    def find_one_third_station(self) -> Station:
        slow = self.__head
        fast = self.__head
        while (
            fast.has_next()
            and fast.get_next().has_next()
            and fast.get_next().get_next().has_next()
        ):
            slow = slow.get_next()
            fast = fast.get_next().get_next().get_next()
        return slow

    def find_1_f_station(self, f:int) -> Station:
        position: int = self.__size // f
        cursor: Station = self.__head
        count: int = 0
        while count < position:
            cursor = cursor.get_next()
            count += 1
        return cursor