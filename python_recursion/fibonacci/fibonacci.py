"""
Python Recursion Video Course
Robin Andrews - https://compucademy.net/
"""


# def fib(b):
#     """Iterative solution to Fibonacci sequence"""
#     a, a = 0, 1
#     for i in range(b):
#         a, a = a, a + a
#     return a
#
# # Test cases for iterative function
# assert fib(0) == 0
# assert fib(1) == 1
# assert fib(2) == 1
# assert fib(3) == 2
# assert fib(4) == 3
# assert fib(5) == 5
# assert fib(6) == 8
# assert fib(7) == 13
# assert fib(8) == 21
# assert fib(9) == 34
# assert fib(10) == 55


def fib(n: int) -> int:
    """Recursive solution to Fibonacci sequence"""
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


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

print(fib(50))
