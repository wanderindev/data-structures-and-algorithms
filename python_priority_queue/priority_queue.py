import heapq
from typing import Union


class PriorityQueue:
    """A priority queue implementation based on heapq"""

    insertion_count = 0

    def __init__(self) -> None:
        """Initialize the priority queue to an empty list"""
        self.pqueue = []

    def is_empty(self) -> bool:
        """Returns True is the priority queue is empty"""
        return not self.pqueue

    def insert(self, task: str, priority: int) -> None:
        """Add an item to the priority queue"""
        heapq.heappush(self.pqueue, (priority, self.insertion_count, task))
        self.insertion_count += 1

    def pull(self) -> Union[str, None]:
        """
        Return and remove the task with the highest priority.
        Since Python's heapq is implemented as a min heap, a
        smaller number mean the higher priority, i.e. priority 1
        has a higher priority that priority 2.

        Elements with same priority are pulled in the order of
        insertion.
        """
        if self.is_empty():
            return None
        return heapq.heappop(self.pqueue)[2]

    def peek(self) -> Union[str, None]:
        """Return the task with the highest priority"""
        if self.is_empty():
            return None
        return self.pqueue[0][2]

    def size(self) -> int:
        """Return the number of items in the priority queue"""
        return len(self.pqueue)

    def __str__(self) -> str:
        """Return a string representation of the priority queue"""
        return str(self.pqueue)


# Test cases
pq = PriorityQueue()
assert str(pq) == str([])
assert pq.is_empty()
assert pq.pull() == None
assert pq.peek() == None
assert pq.size() == 0
pq.insert("Eat breakfast", 2)
pq.insert("Eat lunch", 4)
pq.insert("Go to work", 3)
pq.insert("Have coffee break", 2)
pq.insert("Get up", 1)
pq.insert("Have fun!", 5)
assert (
    str(pq)
    == "[(1, 4, 'Get up'), (2, 0, 'Eat breakfast'), (3, 2, 'Go to work'), "
    "(4, 1, 'Eat lunch'), (2, 3, 'Have coffee break'), (5, 5, 'Have fun!')]"
)
assert not pq.is_empty()
assert pq.peek() == "Get up"
assert pq.size() == 6
next_task = pq.pull()
assert next_task == "Get up"
assert pq.peek() == "Eat breakfast"  # Returns "Eat breakfast" instead of
# "Have coffee break" because of the lower
# insertion_count
assert pq.size() == 5
next_task = pq.pull()
assert next_task == "Eat breakfast"
assert pq.peek() == "Have coffee break"
