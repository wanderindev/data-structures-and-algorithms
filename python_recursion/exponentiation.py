def exp_iterative(a, n):
    base = a
    for i in range(n - 1):
        a *= base
    return a


assert exp_iterative(5, 3) == 125
assert exp_iterative(2, 4) == 16
assert exp_iterative(1, 19) == 1
assert exp_iterative(0, 2) == 0


import time


def exponentation(m: int, n: int) -> float:
    """Recursive solution to exponentiation of a^b"""
    # Base cases
    if m == 0:
        return 0
    if n == 0:
        return 1
    # Recursive cases
    if n > 0:
        return exponentation(m, n - 1) * m
    return 1 / (exponentation(m, abs(n) - 1) * m)


assert exponentation(5, 3) == 125
assert exponentation(2, 4) == 16
assert exponentation(1, 19) == 1
assert exponentation(0, 2) == 0
assert exponentation(5, -2) == 0.04


start = time.perf_counter()
exponentation(10, 5)
end = time.perf_counter()
print(f"Runtime for a exponent of 5. Seconds taken: {(end - start):.7f}")

start = time.perf_counter()
exponentation(10, 10)
end = time.perf_counter()
print(f"Runtime for a exponent of 10. Seconds taken: {(end - start):.7f}")

start = time.perf_counter()
exponentation(10, 20)
end = time.perf_counter()
print(f"Runtime for a exponent of 20. Seconds taken: {(end - start):.7f}")
