import time


def gcd(a: int, b: int) -> int:
    """
    Recursive solution to computing the greatest common divisor of
    two integers a and b
    """
    # Base case
    if b == 0:
        return a
    # Recursive case
    return gcd(b, a % b)


# Test cases for recursive function
assert gcd(8, 12) == 4
assert gcd(45, 10) == 5
assert gcd(47, 13) == 1

start = time.perf_counter()
gcd(8, 6)
end = time.perf_counter()
print(f"Runtime for the gcd of 8 and 12. Seconds taken: {(end - start):.7f}")

start = time.perf_counter()
gcd(800, 120)
end = time.perf_counter()
print(f"Runtime for the gcd of 8 and 24. Seconds taken: {(end - start):.7f}")

start = time.perf_counter()
gcd(16000, 2)
end = time.perf_counter()
print(f"Runtime for the gcd of 8 and 36. Seconds taken: {(end - start):.7f}")
