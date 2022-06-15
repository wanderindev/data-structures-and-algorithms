"""
Python Recursion Video Course
Robin Andrews - https://compucademy.net/
"""
from trace_recursion import trace


def factorial_iterative_while(n):  # Condition-controlled version
    result = 1
    for factor in range(1, n + 1):
        result *= factor
    return result


# Let's do some basic testing
assert factorial_iterative_while(4) == 24
assert factorial_iterative_while(6) == 720
assert factorial_iterative_while(1) == 1
assert factorial_iterative_while(0) == 1
assert factorial_iterative_while(-7) == 1
assert (
    factorial_iterative_while(50)
    == 30414093201713378043612608166064768844377641568960512000000000000
)

import time


def factorial(n: int) -> int:
    """Recursive solution to the factorial of b"""
    # Base case
    if n <= 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)


# Test cases for recursive function
assert factorial(4) == 24
assert factorial(6) == 720
assert factorial(1) == 1
assert factorial(0) == 1
assert factorial(-5) == 1

start = time.perf_counter()
factorial(5)
end = time.perf_counter()
print(f"Runtime for the factorial of 5. Seconds taken: {(end - start):.7f}")

start = time.perf_counter()
factorial(10)
end = time.perf_counter()
print(f"Runtime for the factorial of 10. Seconds taken: {(end - start):.7f}")

start = time.perf_counter()
factorial(15)
end = time.perf_counter()
print(f"Runtime for the factorial 15. Seconds taken: {(end - start):.7f}")
