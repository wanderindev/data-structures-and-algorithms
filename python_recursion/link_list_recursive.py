from typing import Union


class Node:
    """Node class consisting of data and a pointer to the next node"""

    def __init__(
        self,
        data: Union[float, int, str],
        next_node: Union["Node", None] = None,
    ) -> None:
        self.data = data
        self.next_node = next_node


def linked_list_traversal(head: "Node") -> None:
    """Recursive solution to traversing a linked list"""
    # Base case
    if head is None:
        return
    # Recursive case
    print(head.data)
    linked_list_traversal(head.next_node)


elem_1 = Node("Foo")
elem_2 = Node("Bar")
elem_3 = Node(1.75)
elem_4 = Node(75)
elem_1.next_node = elem_2
elem_2.next_node = elem_3
elem_3.next_node = elem_4

linked_list_traversal(elem_1)  # prints Foo Bar 1.75 75
