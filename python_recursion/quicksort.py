import sys
import random
import time
from typing import List


def quicksort(l: List) -> List:
    """Recursive solution to performing quicksort on a list"""
    # Base case
    if len(l) <= 1:
        return l
    # Recursive case
    pivot = l[len(l) // 2]
    left = [x for x in l if x < pivot]
    middle = [x for x in l if x == pivot]
    right = [x for x in l if x > pivot]
    return quicksort(left) + middle + quicksort(right)


# Test cases for recursive function
assert quicksort([5, 1, 8, 6, 9]) == [1, 5, 6, 8, 9]
assert quicksort([]) == []
assert quicksort([1]) == [1]
assert quicksort([-1, -2, 7, 0, 0, -9]) == [-9, -2, -1, 0, 0, 7]

l = random.sample(range(1, 10000), 125)
start = time.perf_counter()
quicksort(l)
end = time.perf_counter()
print(
    f"Runtime for quicksorting all elements in a list of length 125. "
    f"Seconds taken: {(end - start):.7f}"
)

l = random.sample(range(1, 10000), 500)
start = time.perf_counter()
quicksort(l)
end = time.perf_counter()
print(
    f"Runtime for quicksorting all elements in a list of length 500. "
    f"Seconds taken: {(end - start):.7f}"
)

sys.setrecursionlimit(2500)

l = random.sample(range(1, 10000), 2000)
start = time.perf_counter()
quicksort(l)
end = time.perf_counter()
print(
    f"Runtime for quicksorting all elements in a list of length 2000. "
    f"Seconds taken: {(end - start):.7f}"
)
