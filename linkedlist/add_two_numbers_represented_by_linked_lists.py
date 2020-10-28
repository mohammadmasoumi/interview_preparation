"""

Given two numbers represented by two linked lists, write a function that returns the sum list.
The sum list is linked list representation of the addition of two input numbers. It is not allowed to modify the lists.
Also, not allowed to use explicit extra space (Hint: Use Recursion).

Example

Input:
  First List: 5->6->3  // represents number 563
  Second List: 8->4->2 //  represents number 842
Output
  Resultant list: 1->4->0->5  // represents number 1405


@see: https://www.geeksforgeeks.org/sum-of-two-linked-lists/
"""


class LinkedList:
    def __init__(self, value, next_node=None):
        self._value = value
        self._next_node = next_node

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, next_node):
        self._next_node = next_node

    def get_size(self):
        current_node, size = self, 1
        while current_node.next_node:
            current_node = current_node.next_node
            size += 1

        return size

    def reverse(self):
        nodes = []
        current_node = self

        while (True):
            nodes.append(current_node)

            if not current_node.next_node:
                break

            next_node = current_node.next_node
            current_node.next_node = None
            current_node = next_node

        last_node = nodes.pop()
        current_node = last_node
        nodes.reverse()

        node: LinkedList
        for node in nodes:
            current_node.next_node = node
            current_node = node

        return last_node

    def to_list(self):
        array = []

        current_node = self
        while (True):
            array.append(str(current_node.value))
            if not current_node.next_node:
                break
            current_node = current_node.next_node

        return array

    def __str__(self):
        return ",".join(self.to_list())

    __repr__ = __str__


class Subtract:

    @staticmethod
    def fix_sizes(node1: LinkedList, node2: LinkedList) -> tuple:
        node1_size = node1.get_size()
        node2_size = node2.get_size()

        diff_size = node1_size - node2_size

        if diff_size > 0:
            zeroes_node = LinkedList(0, None)
            current_node = zeroes_node

            while (diff_size - 1):
                new_node = LinkedList(0, None)
                current_node.next_node = new_node
                current_node = new_node

                diff_size -= 1

            current_node.next_node = node2
            node2 = zeroes_node

        elif diff_size < 0:
            zeroes_node = LinkedList(0, None)
            current_node = zeroes_node

            while (diff_size + 1):
                new_node = LinkedList(0, None)
                current_node.next_node = new_node
                current_node = new_node

                diff_size += 1

            current_node.next_node = node1
            node1 = zeroes_node

        return node1.reverse(), node2.reverse()

    @staticmethod
    def sum(value1, value2, carry=0):
        summation = value1 + value2 + carry

        new_carry = summation // 10
        new_value = summation % 10

        return new_value, new_carry

    def submission_rec(self, res_node: LinkedList, node1: LinkedList, node2: LinkedList, carry: int) -> int:
        value, next_carry = self.sum(node1.value, node2.value, carry)
        next_res_node = LinkedList(value=value)
        res_node.next_node = next_res_node

        if node1.next_node:
            return self.submission_rec(next_res_node, node1.next_node, node2.next_node, next_carry)

        return next_carry

    def summation(self, linked_list1: LinkedList, linked_list2: LinkedList) -> LinkedList:
        new_node1, new_node2 = self.fix_sizes(node1=linked_list1, node2=linked_list2)

        value, carry = self.sum(new_node1.value, new_node2.value)
        starter_node = LinkedList(value=value)

        last_carry = self.submission_rec(starter_node, new_node1.next_node, new_node2.next_node, carry)

        reversed_res_node = starter_node.reverse()

        return LinkedList(last_carry, reversed_res_node) if last_carry else reversed_res_node


if __name__ == '__main__':
    """ Sample
    4,3,2,1
    4,3
    res_node: 4,3,6,4
    """
    linked_list, linked_list2 = None, None

    number1 = list(map(int, input().strip().split(',')))
    number2 = list(map(int, input().strip().split(',')))

    node_starter1 = LinkedList(value=number1.pop(0))
    node_starter2 = LinkedList(value=number2.pop(0))
    curr_node1, curr_node2 = node_starter1, node_starter2

    for num in number1:
        node = LinkedList(value=num)
        curr_node1.next_node = node
        curr_node1 = node

    for num in number2:
        node = LinkedList(value=num)
        curr_node2.next_node = node
        curr_node2 = node

    res_node = Subtract().summation(node_starter1, node_starter2)

    print(f"res_node: {res_node}")
