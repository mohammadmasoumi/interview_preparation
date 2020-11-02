"""
                 1
               /   \
              2     3
             / \     \
            4   5     6
"""


class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.is_root = False


def print_left_view(root: Node):
    if root is None:
        return False

    if root.is_root:
        print(root.key)

    if root.left:
        print(root.left.key)

    print_left_view(root.left)
    print_left_view(root.right)

    return False


if __name__ == '__main__':
    root = Node(12)
    root.is_root = True
    root.left = Node(10)
    root.right = Node(20)
    root.right.left = Node(25)
    root.right.right = Node(40)
    print_left_view(root)
