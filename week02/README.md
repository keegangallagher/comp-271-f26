# Week 2 Assignment: `Array271` — A Fixed-Capacity Array

## Background

In class this week we defined an array as a **contiguous** block of memory
— that's what makes indexing possible in constant time — and traced that
idea from C's `malloc` through Java's `int[] arr = new int[4]`. Python's
own `list` hides all of this from you: it grows and shrinks automatically,
and it can hold any mix of types.

For this assignment, you'll build a class, `Array271`, that puts that
hidden machinery back in view. `Array271` behaves like a fixed-capacity
array of strings: it reserves a fixed number of slots up front, tracks how
many of them are actually in use, and — the one part you have to write
yourself — grows into a new, larger block when it runs out of room.

## What you're given

`array_271.py`, containing the `Array271` class:

- **`__init__(self, capacity=2, resize_factor=0.25)`** — fully implemented.
  Sets up `capacity`, `resize_factor`, `occupancy` (starts at 0), and
  `items` (a list of length `capacity`, every slot `None`).
- **`add(self, value)`** — fully implemented. Checks whether the array is
  full (`occupancy == capacity`); if so, calls `resize()` first; then
  stores `value` at the next free slot and increments `occupancy`.
- **`resize(self)`** — a `pass` stub. **This is your assignment.**

Read every docstring and comment in the file before you start — they walk
through the reasoning, not just the mechanics, and the `resize` docstring
lays out the exact steps you need to implement.

Also given: `test_array_271.py`, a small set of plain-`assert` checks (no
`unittest` or `pytest` yet — that comes later). Run it with:

```
python3 test_array_271.py
```

Four of the five tests already pass against the file as-is. The last one,
`test_add_triggers_resize`, is your checkpoint — it currently fails with
an `IndexError` because `resize` does nothing yet. When your
implementation is correct, all five should pass.

## What you need to do

Implement `resize(self)` so that it:

1. Computes a new, larger capacity from the current one, using
   `resize_factor` as the fraction to grow by (e.g. `resize_factor=0.25`
   means "grow capacity by 25%"). Decide what to do when that growth
   rounds down to zero additional slots — a small starting capacity like
   2 will hit this immediately — and be ready to explain your choice.
2. Allocates a new list of that new capacity, every slot initialized to
   `None`.
3. Copies every currently-occupied string (indices `0` through
   `occupancy - 1`) from the old `items` into the new one, in the same
   order.
4. Replaces `self.items` with the new list and updates `self.capacity`.
   Leave `self.occupancy` untouched — resizing changes how much room
   there is, not how many strings are stored.

Do not change the signature or behavior of `__init__` or `add`. Do not
import anything — this can and should be done with plain Python.

## Questions to be ready to discuss in class

- Why copy the strings one at a time into a new list, instead of just
  reusing the old one?
- What breaks if you update `self.capacity` *before* finishing the copy?
- With `capacity=2` and `resize_factor=0.25`, what should happen on the
  very first resize? What did you decide, and why?
- Does "resize" ever make sense as *shrinking*? Would `resize_factor`
  still mean the same thing if it did?

## How to submit

Submit your completed `array_271.py` (with `resize` implemented) and
confirm `python3 test_array_271.py` prints `All tests passed.` at the
end.

## Reading

### Assigned

From [Think Python, 3rd edition](https://allendowney.github.io/ThinkPython/),
by Allen Downey:

- [Ch. 9, "Lists"](https://allendowney.github.io/ThinkPython/chap09.html) —
  in full. This is Python's dynamic array — the thing `Array271` is
  deliberately *not* — read it with an eye for which parts of the chapter
  Python normally handles for you automatically that you're now doing by
  hand.
- [Ch. 16, "Classes and Objects"](https://allendowney.github.io/ThinkPython/chap16.html) —
  through the sections on defining a class, `__init__`, and instance
  attributes. This is the material behind `Array271` itself: a class with
  attributes (`capacity`, `occupancy`, `resize_factor`, `items`) set up in
  `__init__`.

From [Introducing Python, 3rd edition](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/),
by Bill Lubanovic (O'Reilly — free on the platform if you log in with your
LUC email):

- [Ch. 8, "Tuples and Lists"](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch08.html) —
  the "Lists" sections only, for now (tuples aren't needed for this
  assignment).
- [Ch. 11, "Objects"](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch11.html) —
  through "Assigning Attributes" and "Initializing an Object with a
  Method" (i.e. `__init__`). The later sections (inheritance, properties,
  magic methods, dataclasses) are beyond what this assignment needs — skim
  or skip them for now.
