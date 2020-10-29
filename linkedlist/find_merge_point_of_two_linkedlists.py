"""
https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem?h_l=interview&playlist
_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=linked-lists&h_r=next-challenge&h_v=zen&h_r=next-challenge&h
_v=zen&h_r=next-challenge&h_v=zen
"""

# !/bin/python3


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def get_size(head):
    size = 0
    current_node = head
    while (True):
        size += 1
        if not current_node.next:
            break

        current_node = current_node.next

    return size


def findMergeNode(head1, head2):
    head1_size = get_size(head1)
    head2_size = get_size(head2)

    diff = head2_size - head1_size

    bigger_head = head2 if diff > 0 else head1
    smaller_head = head1 if diff > 0 else head2

    abs_diff = abs(diff)
    while (abs_diff):
        bigger_head = bigger_head.next
        abs_diff -= 1

    while (True):
        if bigger_head.next and smaller_head.next:
            bigger_head = bigger_head.next
            smaller_head = smaller_head.next
            if id(bigger_head) == id(smaller_head):
                return smaller_head.data
        else:
            return bigger_head.data
