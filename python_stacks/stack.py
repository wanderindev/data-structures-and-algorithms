from collections import deque
from typing import Any


class Stack:
    """A stack implementation based on deque"""

    def __init__(self) -> None:
        """Initialize the stack as an empty deque"""
        self.items = deque()

    def is_empty(self) -> bool:
        """Returns True is the stack is empty"""
        return not self.items

    def push(self, item: Any) -> None:
        """Add an item to the top of the stack"""
        self.items.append(item)

    def pop(self) -> Any:
        """Return and remove the item at the top of the stack"""
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self) -> Any:
        """Return the item at the top of the stack"""
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self) -> int:
        """Return the number of items in the stack"""
        return len(self.items)

    def __str__(self) -> str:
        """Return a string representation of the stack"""
        return str(self.items)


# Test cases
s = Stack()
assert str(s) == "deque([])"
assert s.size() == 0
assert s.is_empty()
assert s.peek() == None
s.push(1)
assert str(s) == "deque([1])"
assert s.size() == 1
assert not s.is_empty()
assert s.peek() == 1
s.push(2)
item = s.pop()
assert item == 2
assert str(s) == "deque([1])"
assert s.size() == 1
assert not s.is_empty()
assert s.peek() == 1
item = s.pop()
item = s.pop()
assert item == None
