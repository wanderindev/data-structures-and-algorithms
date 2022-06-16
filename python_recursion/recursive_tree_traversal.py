from typing import Union


class Node(object):
    """Node class consisting of data and a left / right branches"""

    def __init__(self, data: Union[float, int, str]) -> None:
        self.data = data
        self.left = None
        self.right = None


def preorder_print(root: "Node", path: str = "") -> str:
    """Root -> Left -> Right"""
    if root:
        path += str(root.data) + "-"
        path = preorder_print(root.left, path)
        path = preorder_print(root.right, path)
    return path


def inorder_print(root: "Node", path: str = "") -> str:
    """Left -> Root -> Right"""
    if root:
        path = inorder_print(root.left, path)
        path += str(root.data) + "-"
        path = inorder_print(root.right, path)
    return path


def postorder_print(root: "Node", path: str = "") -> str:
    """Left -> Right -> Root"""
    if root:
        path = postorder_print(root.left, path)
        path = postorder_print(root.right, path)
        path += str(root.data) + "-"
    return path


# Set up tree:
tree_root = Node(6)
tree_root.left = Node(4)
tree_root.left.left = Node(2)
tree_root.left.left.left = Node(1)
tree_root.left.left.right = Node(3)
tree_root.left.right = Node(5)
tree_root.right = Node(10)
tree_root.right.left = Node(8)
tree_root.right.left.left = Node(7)
tree_root.right.left.right = Node(9)
tree_root.right.right = Node(11)

print("Tree graphical representation:")
print(
    """
          ______6______
         /             \\
      __4__           __10__
     /     \         /      \\
    2       5       8        11
   / \             / \\
  1   3           7   9
"""
)

print("Preorder:", preorder_print(tree_root))  # prints 6-4-2-1-3-5-10-8-7-9-11
print("Inorder:", inorder_print(tree_root))  # prints -2-3-4-5-6-7-8-9-10-11
print(
    "Postorder", postorder_print(tree_root)
)  # prints 1-3-2-5-4-7-9-8-11-10-6
