from collections import deque
from typing import Any


class Queue:
    """A queue implementation based on deque"""

    def __init__(self) -> None:
        """Initialize the queue as an empty deque"""
        self.items = deque()

    def is_empty(self) -> bool:
        """Returns True is the queue is empty"""
        return not self.items

    def enqueue(self, item: Any) -> None:
        """Add an item to the back of the queue"""
        self.items.append(item)

    def dequeue(self) -> Any:
        """Return and remove the item at the front of the queue"""
        if self.is_empty():
            return None
        return self.items.popleft()

    def peek(self) -> Any:
        """Return the item at the front of the queue"""
        if self.is_empty():
            return None
        return self.items[0]

    def size(self) -> int:
        """Return the number of items in the queue"""
        return len(self.items)

    def __str__(self) -> str:
        """Return a string representation of the queue"""
        return str(self.items)


# Test cases
q = Queue()
assert str(q) == "deque([])"
assert q.size() == 0
assert q.is_empty()
assert q.peek() == None
q.enqueue(1)
assert str(q) == "deque([1])"
assert q.size() == 1
assert not q.is_empty()
assert q.peek() == 1
q.enqueue(2)
item = q.dequeue()
assert item == 1
assert str(q) == "deque([2])"
assert q.size() == 1
assert not q.is_empty()
assert q.peek() == 2
item = q.dequeue()
item = q.dequeue()
assert item == None
