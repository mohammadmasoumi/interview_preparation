"""
https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/
"""


class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


#     7
#   3   6
#  1 2  5 8

def find_path(root: Node, path, key):
    if root is None:
        return False

    path.append(root.key)
    if root.key == key:
        return True

    left_path = find_path(root.left, path, key) if root.left is not None else None
    right_path = find_path(root.right, path, key) if root.right is not None else None

    if left_path or right_path:
        return True

    path.pop()
    return False


def lca(root, key1, key2):
    path1, path2 = [], []

    if not find_path(root, path1, key1) or not find_path(root, path2, key2):
        return -1
    return len(set(path1).intersection(set(path2)))


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    print("LCA(4, 5) = %d" % (lca(root, 4, 5)))
