"""
Array271 -- a fixed-capacity string array, built on top of a Python list.

This is the Week 2 `Array271` (see `week02/array_271.py`) carried forward
and extended with what we covered in class this week: private attributes
with accessor ("getter") methods instead of reaching into the object
directly, a `__str__` so printing an object shows something useful, a
`resize` that actually works, and a first `remove`.

Encapsulation, in short: every attribute is named with a leading
underscore (`_capacity`, not `capacity`) as a signal of "please don't
reach in here directly" -- Python doesn't enforce this, unlike Java or
C++, so it's a convention we agree to respect, not a wall. Reading or
changing an attribute from outside the class should always go through a
method (a getter, or a method like `add` that changes state on your
behalf).

This file is intentionally incomplete in one place: `remove` works, but
only partially -- see its docstring, and this week's `README.md`, for the
two modifications that are your assignment.
"""

from math import ceil


class Array271:
    """A fixed-capacity array of strings, backed by a Python list.

    Private attributes (leading underscore -- see module docstring):

        _capacity (int):
            How many string slots this array currently has room for,
            whether they're all in use or not.

        _resize_factor (float):
            How aggressively the array grows when it runs out of room.
            Expressed as a fraction of the current capacity to add, e.g.
            0.25 means "grow capacity by 25% when you resize."

        _occupancy (int):
            How many slots are actually holding a string right now.
            Always satisfies 0 <= occupancy <= capacity.

        _items (list):
            The underlying Python list that actually stores the strings.
            Pre-sized to `_capacity` and padded with None past the last
            occupied slot -- treat index `_occupancy` and beyond as empty,
            even though Python itself doesn't enforce that for us.
    """

    def __init__(self, capacity: int = 2, resize_factor: float = 0.25):
        self.__capacity: int = capacity
        self.__resize_factor: float = resize_factor
        self.__occupancy: int = 0
        self.__items: list = [None] * capacity

    def __str__(self):
        return f"Array271(capacity={self.__capacity}, resize_factor={self.__resize_factor}, occupancy={self.__occupancy}, items={self.__items})"

    def get_capacity(self):
        return self.__capacity
    def get_resize_factor(self):
        return self.__resize_factor
    def get_occupancy(self):
        return self.__occupancy
    def get_items(self):
        return self.__items

    def get_item(self, i):
        item = None
        if i >=0 and i < self.__occupancy:
            item = self.__items[i]
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
