"""
https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem?h_l=interview&playlist_slugs%5B%5D=interv
iew-preparation-kit&playlist_slugs%5B%5D=linked-lists&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
"""
# !/bin/python3


class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node


def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


# Complete the reverse function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def reverse(head):
    nodes = []

    current_node = head
    while (True):
        nodes.append(current_node)

        if not current_node.next:
            break

        current_node = current_node.next

    if nodes:
        head_node = nodes.pop()
        head_node.prev = None
    else:
        head_node = None

    prev_node = head_node
    while (len(nodes)):
        node = nodes.pop()
        prev_node.next = node
        node.next = None
        node.prev = prev_node
        prev_node = node

    return head_node
