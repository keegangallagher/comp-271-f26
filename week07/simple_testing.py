"""A simple timing harness for the Week 7 mystery sorters.

For each mystery function, this script starts with a small list, times the
function on it, then ADDS a fixed step to n and times it again, over and over.
For every n it prints one line: the size, and the average time one call took.
You then look at how those times grow as n grows.

Run it from a terminal with:

    python3 simple_testing.py

You are free to change this file: different sizes, different trial counts,
a different step. The assignment asks you to explain HOW you timed things,
so make sure you understand every line before you hand in results produced
by it. See the Week 7 README for the method and why it is set up this way.
"""

import random
import signal
import time

# The package you installed with `pip install comp271-mystery-sorters`.
# Each name below is a function that takes a list of ints and returns a new,
# sorted list. We only ever call them; we never look inside them.
from comp271_mystery_sorters import gandalf, saruman, sauron

# How many times we time the function at each size. A single run is one
# sample, not a measurement: the computer is busy with other things, and
# different random lists can behave differently. Averaging several runs
# smooths that noise out.
TRIALS = 10

# How many seconds we allow ourselves to spend on ALL the trials at one
# value of n. Once a size costs more than this, we stop testing that
# function. Without a limit like this, a function that grows quickly would
# make us wait a very long time.
TIME_LIMIT = 0.5


def random_array(n: int) -> list[int]:
    """Build a list of n random integers between 0 and 10,000.

    A fresh list is built for every trial, so the average is not just a
    statement about one lucky (or unlucky) arrangement of numbers.
    """
    return [random.randint(0, 10_000) for _ in range(n)]


def average_time(func, n: int) -> float | None:
    """Time func on TRIALS random lists of size n.

    Returns the average time of one call, in seconds, or None if any call
    ran past PER_CALL_LIMIT and was interrupted.
    """
    signal.signal(signal.SIGALRM, interrupt_call)
    total = 0.0
    trial = 0
    finished = True
    while trial < TRIALS and finished:
        data = random_array(n)

        # Start the alarm; it goes off if the call below runs too long.
        signal.alarm(PER_CALL_LIMIT)
        try:
            # Use time.perf_counter(), not time.time(): it is designed for
            # measuring short intervals and has much finer resolution.
            # Only the call to func sits between the two readings, so
            # building the random list is NOT included in the measured time.
            start = time.perf_counter()
            func(data)
            total += time.perf_counter() - start
            trial += 1
        except CallTooSlow:
            finished = False
        finally:
            # Cancel the alarm whether the call finished or was interrupted.
            signal.alarm(0)

    average = None
    if finished:
        average = total / TRIALS
    return average


# Everything below runs only when you execute this file directly
# (python3 simple_testing.py), not when another file imports it.
if __name__ == "__main__":

    # Work through the functions one at a time. Each function starts over
    # at its own starting size and is dropped once it crosses either limit,
    # before we move on to the next one.
    for function in [gandalf, saruman, sauron]:
        print(function.__name__)

        n, step = SETTINGS[function.__name__]
        function_start = time.perf_counter()
        keep_going = True

        while keep_going:
            avg = average_time(function, n)

            # One line per size: n, then the average seconds per call.
            # The :.6f formats the time with six digits after the decimal
            # point, so very small times still show up as nonzero.
            print(n, f"{avg:.6f}")

                # Rule 2: the total time on this function.
                if time.perf_counter() - function_start > TOTAL_LIMIT:
                    print(f"stopped at n = {n}: more than {TOTAL_LIMIT} "
                          f"seconds spent on this function")
                    keep_going = False
                else:
                    # Add the step for the next round: 16, 18, 20, ...
                    # We write the exit as a condition instead of using
                    # `break`, so the loop has a single, obvious exit.
                    n += step
