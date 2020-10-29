"""
https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=linked-lists
"""
import math
import os
import random
import re
import sys


class SinglyLinkedList:

    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.head = self

    def insert_node(self, value, pos=None):
        if not self.data:
            self.data = value
        else:
            current_node = self
            current_idx = 1
            node = SinglyLinkedList(data=value)

            while (True):

                if not current_node.next:
                    current_node.next = node
                    break

                elif pos and pos == current_idx:
                    detach_node = current_node.next
                    node.next = detach_node
                    current_node.next = node
                    break

                current_idx += 1
                current_node = current_node.next


def insertNodeAtPosition(head, data, position):
    if position == 0:
        node = SinglyLinkedList(data=data)
        node.next = head
        return node

    head.insert_node(data, position)

    return head
