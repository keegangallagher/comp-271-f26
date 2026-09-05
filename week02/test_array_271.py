"""
Simple, plain-Python tests for Array271 (array_271.py).

We are not using unittest, pytest, or any testing framework yet -- that
comes later in the course. For now, each test is just a function that
uses `assert` statements to check that something is true. If an assert
fails, Python raises an AssertionError and prints exactly which line
failed, which is enough to tell us something is wrong.

How to run this file:
    python3 test_array_271.py

Every test that passes will print an "ok" line. The very last test in
this file (test_add_triggers_resize) is EXPECTED TO FAIL until you
implement the `resize` method -- that's on purpose. It's your checkpoint
for knowing when `resize` is working.
"""

from array_271 import Array271


def test_default_construction():
    """A freshly constructed array should use the default capacity (2)
    and resize_factor (0.25), start empty, and pre-fill its storage with
    None placeholders."""
    arr = Array271()

    assert arr.capacity == 2, "default capacity should be 2"
    assert arr.resize_factor == 0.25, "default resize_factor should be 0.25"
    assert arr.occupancy == 0, "a brand-new array should start with occupancy 0"
    assert arr.items == [None, None], "items should be pre-sized to capacity, all None"

    print("ok: test_default_construction")


def test_custom_construction():
    """The constructor should honor whatever capacity and resize_factor
    are passed in, instead of always using the defaults."""
    arr = Array271(capacity=5, resize_factor=0.5)

    assert arr.capacity == 5
    assert arr.resize_factor == 0.5
    assert arr.occupancy == 0
    assert arr.items == [None, None, None, None, None]

    print("ok: test_custom_construction")


def test_add_single_item_without_resizing():
    """Adding one string to an array that has room should not need to
    resize at all -- it should just occupy the next free slot and bump
    occupancy by one."""
    arr = Array271(capacity=3, resize_factor=0.25)

    arr.add("Mississippi")

    assert arr.occupancy == 1, "occupancy should go up by 1 after one add"
    assert arr.capacity == 3, "capacity should be unchanged -- there was room"
    assert arr.items[0] == "Mississippi", "the new string should land in slot 0"
    assert arr.items[1] is None, "unused slots should still be None"
    assert arr.items[2] is None, "unused slots should still be None"

    print("ok: test_add_single_item_without_resizing")


def test_add_multiple_items_fills_slots_in_order():
    """Repeated adds should fill slots left to right, in the order the
    strings were added, without disturbing earlier entries."""
    arr = Array271(capacity=4, resize_factor=0.25)

    arr.add("M")
    arr.add("i")
    arr.add("s")

    assert arr.occupancy == 3
    assert arr.items[0] == "M"
    assert arr.items[1] == "i"
    assert arr.items[2] == "s"
    assert arr.items[3] is None

    print("ok: test_add_multiple_items_fills_slots_in_order")


def test_add_triggers_resize():
    """This is the checkpoint test for `resize`.

    With the default capacity of 2, adding a THIRD string should force
    the array to grow: `add` will notice occupancy == capacity and call
    `resize()`. Until you implement `resize`, this test will fail with
    an IndexError, because the underlying list is still only 2 slots
    long. Once `resize` is implemented correctly, this test should pass:
    capacity should have grown, all three strings should be present and
    in order, and occupancy should correctly reflect 3 items stored.
    """
    arr = Array271()  # capacity=2, resize_factor=0.25

    arr.add("this")
    arr.add("is")
    arr.add("full")  # this add should trigger a resize

    assert arr.capacity > 2, "capacity should have grown past the original 2"
    assert arr.occupancy == 3, "occupancy should be 3 after three successful adds"
    assert arr.items[0] == "this"
    assert arr.items[1] == "is"
    assert arr.items[2] == "full"

    print("ok: test_add_triggers_resize")


if __name__ == "__main__":
    test_default_construction()
    test_custom_construction()
    test_add_single_item_without_resizing()
    test_add_multiple_items_fills_slots_in_order()
    test_add_triggers_resize()

    print("\nAll tests passed.")
