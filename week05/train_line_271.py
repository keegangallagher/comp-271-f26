"""
TrainLine271: the BetterTrainLine we wrote in class on 9/25, promoted to
a full member of the 271 family by honoring the OurContract interface.

A train line is a chain of Station objects. The line itself remembers
only two of them: the head (the first station) and the last station.
Every other station is reached by starting at the head and following
get_next() one station at a time -- no skipping ahead.

Whoever uses a TrainLine271 works with station NAMES (strings), never
with Station objects. add("Howard") builds the Station itself; searches
take a name and report positions. The Station class is an internal
detail of the line, the same way the underlying list is an internal
detail of Array271.

Positions are counted from the head, starting at 0: on the line
Howard -> Jarvis -> Morse, Howard is at 0 and Morse is at 2.

Your job: replace every "TODO" below. Do not change the signatures.
Follow the course rules: one return statement per method, no break, no
imports beyond abc, typing, __future__, OurContract, and Station, no
magic numbers.
"""

from __future__ import annotations

from OurContract import OurContract
from Station import Station


class TrainLine271(OurContract):

    def __init__(self, name: str):
        self.__name: str = name
        self.__head: Station = None
        self.__last: Station = None

    def __str__(self) -> str:
        return f"Train line name: {self.__name}"

    def get_name(self) -> str:
        return self.__name

    def add(self, value: str) -> None:
        # TODO: wrap value in a new Station and attach it after the last
        # station, the BetterTrainLine way -- a fixed number of steps no
        # matter how long the line is. An empty line is the special case.
        new_station = Station(value)

        if self.__head == None:
            self.__head = new_station
            

        else:
            self.__last.set_next(new_station)
            
        
        self.__last = new_station
                 

    def contains(self, value: str) -> bool:
        # TODO: delegate to index_of, as we did in class.
        if self.index_of(value) == []:
            contains = False
        else:
            contains = True

        return contains 


    def index_of(self, value: str) -> list:
        # TODO: return a one-element list with the position of the FIRST
        # station named value, e.g. [2], or an empty list [] if there is
        # no such station. Stop walking as soon as you find it.
        rider: Station = self.__head
        location = []
        count = 0

        while rider is not None and rider.get_name() != value:
            rider = rider.get_next()
            count += 1

        if rider != None:
            location.append(count)

        return location 
    

    def indices(self, value: str) -> list:
        # TODO: return a list with the position of EVERY station named
        # value, front to back, e.g. [1, 4], or [] if there is none.
        indicies = []
        rider: Station = self.__head 
        count = 0

        while rider is not None:
            if rider.get_name() == value:
                indicies.append(count)

            rider = rider.get_next()
            count += 1

        return indicies

    def count(self, value: str) -> int:
        # TODO: how many stations are named value.
        count = 0 
        rider: Station = self.__head

        while rider != None:
            if rider.get_name() == value:
                count += 1

            rider = rider.get_next()

        return count

        
