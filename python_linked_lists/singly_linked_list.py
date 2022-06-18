from typing import Any, Union


class Node:
    """A linked list node implementation"""

    def __init__(self, node_data: Any) -> None:
        """Initialize the node with the given data and pointing to None"""
        self._data = node_data
        self._next_node = None

    def __str__(self) -> str:
        """Return a string representation of the node"""
        return str(self.data)

    @property
    def data(self) -> Any:
        """Returns the node's data"""
        return self._data

    @data.setter
    def data(self, node_data: Any) -> None:
        """Replaces the node's data with the given data"""
        self._data = node_data

    @property
    def next_node(self) -> Union["Node", None]:
        """Returns the node's next"""
        return self._next_node

    @next_node.setter
    def next_node(self, next_node: Union["Node", None]) -> None:
        """Replaces the node's data with the given data"""
        self._next_node = next_node


class SinglyLinkedList:
    """A singly linked list implementation"""

    def __init__(self) -> None:
        """Initialize a singly link list where the head is None"""
        self.head = None

    def __str__(self) -> str:
        """Return a string representation of the linked list"""
        sll_nodes = []
        current_node = self.head
        while current_node is not None:
            sll_nodes.append(str(current_node.data))
            current_node = current_node.next_node
        sll_nodes.append(str(None))
        return " -> ".join(sll_nodes)

    def is_empty(self) -> bool:
        """Returns True is the linked list is empty"""
        return not self.head

    def get_last_node(self) -> "Node":
        """Return the last node in the linked list"""
        current_node = self.head
        while current_node.next_node is not None:
            current_node = current_node.next_node
        return current_node

    def get_node(self, node_data: Any) -> Union["Node", None]:
        """Return the first node whose data is node_data or None"""
        current_node = self.head
        while current_node.data != node_data:
            if not current_node:
                return None
            current_node = current_node.next_node
        return current_node

    def get_prev_node(self, node_data: Any) -> Union["Node", None]:
        """Return the node before first node whose data is node_data or None"""
        current_node = self.head
        prev_node = None
        while current_node.data != node_data:
            if not current_node:
                return None
            prev_node = current_node
            current_node = current_node.next_node
        return prev_node

    def add_front(self, new_data: Any) -> None:
        """Add a node to the front of the linked list"""
        new_node = Node(new_data)
        new_node.next_node = self.head
        self.head = new_node

    def add_back(self, new_data: Any) -> None:
        """Add a node to the back of the linked list"""
        self.get_last_node().next_node = Node(new_data)

    def add_after(self, node_data: Any, new_data: Any) -> None:
        """Add a node after the first node whose data is node_data"""
        new_node = Node(new_data)
        insert_at_node = self.get_node(node_data)
        if insert_at_node:
            new_node.next_node = insert_at_node.next_node
            insert_at_node.next_node = new_node

    def add_before(self, node_data: Any, new_data: Any) -> None:
        """Add a node before the first node whose data is node_data"""
        new_node = Node(new_data)
        insert_at_node = self.get_prev_node(node_data)
        if insert_at_node:
            new_node.next_node = insert_at_node.next_node
            insert_at_node.next_node = new_node
        else:
            self.add_front(new_data)

    def pop(self) -> Union[Any, None]:
        """Return and remove the node at the front of the linked list"""
        if self.is_empty():
            return None
        node_to_pop = self.head
        self.head = self.head.next_node
        return node_to_pop.data

    def remove(self, node_data: Any) -> None:
        """Remove the first node whose data is node_data"""
        if not self.is_empty():
            prev_node = self.get_prev_node(node_data)
            prev_node.next_node = prev_node.next_node.next_node

    def size(self) -> int:
        """Traverses the linked list and returns the number of nodes in it"""
        if self.is_empty():
            return 0
        size = 0
        current_node = self.head
        while current_node is not None:
            current_node = current_node.next_node
            size += 1
        return size


# Test cases for the Node class
node_1 = Node("Foo")
node_2 = Node(3.14159)
node_3 = Node([1, 2, 3])
node_1.next_node = node_2
node_2.next_node = node_3
assert str(node_1) == "Foo"
assert str(node_1.next_node) == "3.14159"
assert str(node_2) == "3.14159"
assert str(node_2.next_node) == "[1, 2, 3]"
assert str(node_3) == "[1, 2, 3]"
assert str(node_3.next_node) == "None"
node_1.data = "Bar"
assert str(node_1) == "Bar"

# Test cases for the SinglyLinkedList class
sll = SinglyLinkedList()
assert str(sll) == str(None)
assert sll.is_empty()
assert sll.size() == 0
assert not sll.pop()
sll.add_front("Baz")
assert str(sll) == "Baz -> None"
sll.add_back(55)
assert str(sll) == "Baz -> 55 -> None"
sll.add_after("Baz", "Foo")
assert str(sll) == "Baz -> Foo -> 55 -> None"
sll.add_before(55, "Bar")
assert str(sll) == "Baz -> Foo -> Bar -> 55 -> None"
data = sll.pop()
assert str(data) == "Baz"
assert str(sll) == "Foo -> Bar -> 55 -> None"
sll.remove("Bar")
assert str(sll) == "Foo -> 55 -> None"
