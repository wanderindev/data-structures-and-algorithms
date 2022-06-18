from typing import Any, Union


class Node:
    """A linked list node implementation"""

    def __init__(self, node_data: Any) -> None:
        """Initialize the node with the given data and pointing to None"""
        self._data = node_data
        self._next_node = None
        self._prev_node = None

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

    @property
    def prev_node(self) -> Union["Node", None]:
        """Returns the node's next"""
        return self._prev_node

    @prev_node.setter
    def prev_node(self, prev_node: Union["Node", None]) -> None:
        """Replaces the node's data with the given data"""
        self._prev_node = prev_node


class DoublyLinkedList:
    """A doubly linked list implementation"""

    def __init__(self) -> None:
        """Initialize a doubly link list where the head is None"""
        self.head = None

    def __str__(self) -> str:
        """Return a string representation of the linked list"""
        dll_nodes = []
        current_node = self.head
        while current_node is not None:
            dll_nodes.append(str(current_node.data))
            current_node = current_node.next_node
        dll_nodes.append(str(None))
        return " <==> ".join(dll_nodes)

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

    def add_front(self, new_data: Any) -> None:
        """Add a node to the front of the linked list"""
        new_node = Node(new_data)
        new_node.next_node = self.head
        if self.head is not None:
            self.head.prev_node = new_node
        self.head = new_node

    def add_back(self, new_data: Any) -> None:
        """Add a node to the back of the linked list"""
        last_node = self.get_last_node()
        new_node = Node(new_data)
        new_node.next_node = last_node.next_node
        new_node.prev_node = last_node
        last_node.next_node = new_node

    def add_after(self, node_data: Any, new_data: Any) -> None:
        """Add a node after the first node whose data is node_data"""
        new_node = Node(new_data)
        insert_at_node = self.get_node(node_data)
        if insert_at_node:
            new_node.next_node = insert_at_node.next_node
            new_node.prev_node = insert_at_node
            insert_at_node.next_node.prev_node = new_node
            insert_at_node.next_node = new_node

    def add_before(self, node_data: Any, new_data: Any) -> None:
        """Add a node before the first node whose data is node_data"""
        new_node = Node(new_data)
        insert_at_node = self.get_node(node_data)
        if insert_at_node:
            new_node.next_node = insert_at_node
            new_node.prev_node = insert_at_node.prev_node
            insert_at_node.prev_node.next_node = new_node
            insert_at_node.prev_node = new_node

    def pop(self) -> Union[Any, None]:
        """Return and remove the node at the front of the linked list"""
        if self.is_empty():
            return None
        node_to_pop = self.head
        self.head = self.head.next_node
        self.head.prev_node = None
        return node_to_pop.data

    def remove(self, node_data: Any) -> None:
        """Remove the first node whose data is node_data"""
        if not self.is_empty():
            node_to_remove = self.get_node(node_data)
            node_to_remove.next_node.prev_node = node_to_remove.prev_node
            node_to_remove.prev_node.next_node = node_to_remove.next_node

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
node_2.prev_node = node_1
node_3.prev_node = node_2
assert str(node_1) == "Foo"
assert str(node_1.next_node) == "3.14159"
assert str(node_1.prev_node) == "None"
assert str(node_2) == "3.14159"
assert str(node_2.next_node) == "[1, 2, 3]"
assert str(node_2.prev_node) == "Foo"
assert str(node_3) == "[1, 2, 3]"
assert str(node_3.next_node) == "None"
assert str(node_3.prev_node) == "3.14159"
node_1.data = "Bar"
assert str(node_1) == "Bar"

# Test cases for the SinglyLinkedList class
dll = DoublyLinkedList()
assert str(dll) == str(None)
assert dll.is_empty()
assert dll.size() == 0
assert not dll.pop()
dll.add_front("Baz")
assert str(dll) == "Baz <==> None"
dll.add_back(55)
assert str(dll) == "Baz <==> 55 <==> None"
dll.add_after("Baz", "Foo")
assert str(dll) == "Baz <==> Foo <==> 55 <==> None"
dll.add_before(55, "Bar")
assert str(dll) == "Baz <==> Foo <==> Bar <==> 55 <==> None"
data = dll.pop()
assert str(data) == "Baz"
assert str(dll) == "Foo <==> Bar <==> 55 <==> None"
dll.remove("Bar")
assert str(dll) == "Foo <==> 55 <==> None"
