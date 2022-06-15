import time
import sys


def string_length(s: str) -> int:
    """Recursive solution to counting the characters of a string"""
    # Base case
    if len(s) <= 1:
        return len(s)
    # Recursive case
    return string_length(s[1:]) + 1


# Test cases for recursive function
assert string_length("Hello world of recursion!") == 25
assert string_length("") == 0
assert string_length(" ") == 1

s = "x" * 125
start = time.perf_counter()
string_length(s)
end = time.perf_counter()
print(
    f"Runtime for counting the number of characters in a str of length 125. "
    f"Seconds taken: {(end - start):.7f}"
)

s = "x" * 500
start = time.perf_counter()
string_length(s)
end = time.perf_counter()
print(
    f"Runtime for counting the number of characters in a str of length 500. "
    f"Seconds taken: {(end - start):.7f}"
)

sys.setrecursionlimit(2500)

s = "x" * 2000
start = time.perf_counter()
string_length(s)
end = time.perf_counter()
print(
    f"Runtime for counting the number of characters in a str of length 2000. "
    f"Seconds taken: {(end - start):.7f}"
)
