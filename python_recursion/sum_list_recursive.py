import time
import sys
from typing import List


def list_sum(l: List) -> float:
    """
    Recursive solution to computing the sum of all pqueue in a
    list of numbers
    """
    # Base case
    if len(l) == 0:
        return 0
    # Recursive case
    return l[0] + list_sum(l[1:])


# Test cases for recursive function
assert list_sum([1, 2, 3, 4]) == 10
assert list_sum([-1, -2, -3, 1, 2]) == -3
assert list_sum([]) == 0
assert list_sum([3.5, 4.5]) == 8

l = [x for x in range(125)]
start = time.perf_counter()
list_sum(l)
end = time.perf_counter()
print(
    f"Runtime for the sum of all pqueue in a list of length 125. "
    f"Seconds taken: {(end - start):.7f}"
)

l = [x for x in range(500)]
start = time.perf_counter()
list_sum(l)
end = time.perf_counter()
print(
    f"Runtime for the sum of all pqueue in a list of length 500. "
    f"Seconds taken: {(end - start):.7f}"
)

sys.setrecursionlimit(2500)

l = [x for x in range(2000)]
start = time.perf_counter()
list_sum(l)
end = time.perf_counter()
print(
    f"Runtime for the sum of all pqueue in a list of length 2000. "
    f"Seconds taken: {(end - start):.7f}"
)
