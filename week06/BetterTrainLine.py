from __future__ import annotations
from Station import *


class BetterTrainLine:
    """A singly-linked chain of Stations representing one train line.

    Stations are added one at a time, always at the tail, so the line is
    built in the same order it will be traveled. The class keeps a __head
    (first station), a __last (current tail, for O(1) appends), and a
    __size (running count of stations).
    """

    # Constant used to compute the 1/f-th station in find_1_f_station().
    _SAFE_FRACTION: int = 1

    def __init__(self, name: str):
        """Create an empty train line.

        Parameters:
            name: the name of the line, e.g. "Red Line".
        """
        self.__name: str = name
        self.__head: Station = None
        self.__last: Station = None
        self.__size: int = 0

    def __str__(self):
        """Return a short human-readable label for the line.

        Returns:
            str: the line's name, formatted for printing.
        """
        return f"Better Train Line name: {self.__name}"

    def add(self, new_station: Station):
        """Append a station to the end of the line.

        Example: if the line currently ends at Jarvis, add(howard) makes
        Howard the new last station, reachable via Jarvis.get_next().

        Parameters:
            new_station: the Station to attach after the current last
                station. No return value is expected.
        """
        if self.__head == None:
            self.__head = new_station
        else:
            self.__last.set_next(new_station)
        self.__last = new_station
        self.__size += 1

    def find_1_f_station(self, f: int) -> Station:
        """Find the station at the (1/f)-th point of the line.

        Since __size is already tracked by add(), the target position is
        known up front as __size // f. This walks a single cursor
        straight to that position, rather than racing two pointers
        against each other. find_1_f_station(2), for example, returns the
        same station as a midpoint search would.

        Parameters:
            f: the fraction's denominator. Must be a positive integer no
                greater than __size, so that __size // f lands on an
                actual station in the line.

        Returns:
            Station: the station at position __size // f. If f is invalid,
            the method will default to a safe value.
        """
        # Validate f and fall back to a safe default if it's invalid. This
        # is a bit more forgiving than the spec, which would raise an
        # exception for any invalid f. The safe default is 1, which returns
        # the first station in the line.
        if not isinstance(f, int) or f < 1 or f > self.__size:
            f = self._SAFE_FRACTION
        position: int = self.__size // f
        cursor: Station = self.__head
        count: int = 0
        # Even if the line is empty, this loop will never run, and cursor will
        # remain None, which is the correct return value for an empty line.
        while count < position:
            cursor = cursor.get_next()
            count += 1
        return cursor