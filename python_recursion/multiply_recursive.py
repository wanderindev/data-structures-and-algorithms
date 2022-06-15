import time


def multiply(m: int, n: int) -> int:
    """Recursive solution to multiplication of a x b"""
    # Base case
    if m == 0 or n == 0:
        return 0
    # Recursive case
    if n < 0:
        return -m + multiply(m, n + 1)
    else:
        return m + multiply(m, n - 1)


# Test cases for recursive function
assert multiply(5, 4) == 20
assert multiply(-3, 2) == -6
assert multiply(6, -3) == -18
assert multiply(-2, -4) == 8
assert multiply(0, 0) == 0

start = time.perf_counter()
multiply(10, 20)
end = time.perf_counter()
print(f"Runtime for a multiplier of 20. Seconds taken: {(end - start):.7f}")

start = time.perf_counter()
multiply(10, 40)
end = time.perf_counter()
print(f"Runtime for a multiplier of 40. Seconds taken: {(end - start):.7f}")

start = time.perf_counter()
multiply(10, 80)
end = time.perf_counter()
print(f"Runtime ffor a multiplier of 80. Seconds taken: {(end - start):.7f}")
