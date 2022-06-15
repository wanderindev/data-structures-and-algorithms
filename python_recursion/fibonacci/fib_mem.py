import time


def fib(n: int, cache: dict = {}) -> int:
    """Recursive solution to Fibonacci sequence using memoization"""
    if n in cache:
        return cache[n]
    if n == 0 or n == 1:
        return n
    cache[n] = fib(n - 1, cache) + fib(n - 2, cache)
    return cache[n]


# Test cases for recursive function
assert fib(0) == 0
assert fib(1) == 1
assert fib(2) == 1
assert fib(3) == 2
assert fib(4) == 3
assert fib(5) == 5
assert fib(6) == 8
assert fib(7) == 13
assert fib(8) == 21
assert fib(9) == 34
assert fib(10) == 55

start = time.perf_counter()
fib(10)
end = time.perf_counter()
print(f"Runtime for 10th Fibonacci number. Seconds taken: {(end - start):.7f}")

start = time.perf_counter()
fib(20)
end = time.perf_counter()
print(f"Runtime for 20th Fibonacci number. Seconds taken: {(end - start):.7f}")

start = time.perf_counter()
fib(40)
end = time.perf_counter()
print(f"Runtime for 40th Fibonacci number. Seconds taken: {(end - start):.7f}")
