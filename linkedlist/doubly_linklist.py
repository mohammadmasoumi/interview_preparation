"""
https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem?h_l=interview&playlist_
slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=linked-lists&h_r=next-challenge&h_v=zen
"""
# !/bin/python3

import math
import os
import random
import re
import sys


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


# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    current_node = head
    node = DoublyLinkedListNode(node_data=data)

    while (True):
        # 1,2,3,4,5, 7
        print(current_node.data)

        if current_node.data > node.data:
            temp_node = current_node.prev
            if temp_node:
                temp_node.next = node
                node.prev = temp_node
            else:
                head = node

            node.next = current_node
            current_node.prev = node
            break

        elif not current_node.next:
            node.prev = current_node
            current_node.next = node
            break

        current_node = current_node.next

    return head
