# Week 6 Assignment: Generalizing the Fast/Slow Sweep, Plus `add_list` and `get_names`

## The task

In class we wrote two methods on `BetterTrainLine`, both using the same
fast/slow trick: `find_middle_station` (fast moves 2 stations per
iteration) and `find_one_third_station` (fast moves 3). Each one is a
single traversal — no counting the line first, no division.

This week you write three methods: one that makes those two a special
case of one idea, one that makes building a line less repetitive, and
one that turns a line back into something you can print, loop over, or
compare at a glance.

## What you're given

- `better_train_line_271.py` — the scaffold. `__init__`, `__str__`, `add`,
  `find_middle_station`, and `find_one_third_station` are complete and
  unchanged from class. `add_list`, `get_names`, and `find_1_f_station`
  are `TODO`.
- `Station.py` — unchanged from class.

Run the scaffold directly to see the given methods work:

```
python3 better_train_line_271.py
```

## What you need to do

### 1. `add_list(names)`

Every line built so far has been built one `add` call per station. Write
`add_list(names)` so it takes a list of strings and adds one station per
name, in order — `add_list(["Howard", "Jarvis", "Morse"])` should have
the exact same effect as calling `add` three times in a row.

- Don't duplicate `add`'s head/last-pointer logic. Build each `Station`
  and hand it to `self.add(...)`.

### 2. `get_names()`

Write `get_names()` so it walks the whole line, head to last, and
returns a list of every station's name, in the order you visited them —
`get_names()` on `Howard -> Jarvis -> Morse` returns
`["Howard", "Jarvis", "Morse"]`.

- This is the same traversal shape you've used all along (start at the
  head, move with `get_next()`, stop when `has_next()` is false) — the
  only difference is you're visiting every station instead of skipping
  ahead, and collecting a name at each stop instead of searching for
  one.

### 3. `find_1_f_station(f)`

Write the method that makes `find_middle_station` and
`find_one_third_station` a special case of one idea:
`find_1_f_station(f)` finds the station 1/f of the way down the line for
whatever `f` you're given. `find_1_f_station(2)` should land on the same
station as `find_middle_station()`; `find_1_f_station(3)` should land on
the same station as `find_one_third_station()`.

**The catch:** you may not use `self.__size` or `//` anywhere in this
method. The whole point is the traversal — fast hopping `f` stations for
every one station slow takes — not computing a position number in
advance and walking straight to it.

- Use the same `slow`/`fast` pattern as `find_middle_station` and
  `find_one_third_station`: `slow` advances one station per iteration;
  `fast` advances `f` stations per iteration.
- Stop as soon as `fast` can't complete one more full `f`-station hop —
  the same idea as `fast.has_next() and fast.get_next().has_next()` in
  `find_middle_station`, just generalized to `f` steps instead of 2.
- You can assume `f` is a positive integer; no need to validate it or
  handle an empty line for this assignment.
- Check your work against the given methods: on
  `Howard -> Jarvis -> Morse -> Loyola -> Granville`,
  `find_1_f_station(2)` should print `Morse` (matching
  `find_middle_station`) and `find_1_f_station(3)` should print `Jarvis`
  (matching `find_one_third_station`).

**Rules, same as class:** one `return` per method; no `break`; talk to a
`Station` only through its methods (`get_name`, `get_next`, `has_next`,
`set_next`), never its private fields; do not change `Station.py`, the
given methods, or any method signature.

## Questions to be ready to discuss in class

- `add_list` could walk `names` and call `self.add(...)` each time, or
  it could try to reuse `__last` directly without going through `add`.
  Why is going through `add` the safer choice, even though it's "one
  more function call" per station?
- `get_names()` and `__str__` both turn a line into something printable,
  but `__str__` doesn't call `get_names()`. Would it make sense for it
  to? What would change about what gets printed?
- Where exactly in your `find_1_f_station` loop condition does the
  number `f` appear, and how does that compare to the hard-coded `2` and
  `3` in the two given methods?
- Why doesn't `find_1_f_station` need `self.__size` at all? What would
  you have to do differently if you *did* want to use it?
- For a line whose length is an exact multiple of `f` (say 9 stations,
  `f=3`), does your method land on the same station that
  `self.__size // f` would predict? Trace it by hand and see.
- `find_middle_station` and `find_one_third_station` could now be
  rewritten as one-line calls to `find_1_f_station`. What would be
  gained — and what, if anything, would be lost — by actually deleting
  them in favor of the general version?

## How to submit

Submit your completed `better_train_line_271.py`. Confirm it still prints
correctly with:

```
python3 better_train_line_271.py
```

Due **Friday, October 9**, via Sakai.
