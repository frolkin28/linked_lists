from linked_list import List
from copy import copy


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class UndirectionalList(List):

    def __init__(self):
            self.head = None

    def insert_to_begin(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node

    def insert_to_end(self, node):
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    def insert_to_middle(self, node, index):
        previous = self.head
        current = previous.next
        for i in range(1, index):
            previous = previous.next
            current = current.next
        previous.next = node
        node.next = current

    def delete_from_begin(self):
        current = self.head
        self.head = current.next

    def delete_from_middle(self, index):
        previous = self.head
        current = previous.next
        for i in range(1, index):
            previous = previous.next
            current = current.next
        previous.next = current.next
        current = None

    def delete_from_end(self):
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def sub_from_begin(self, node):
        if self.head:
            current = self.head
            node.next = current.next
        self.head = node

    def sub_from_middle(self, node, index):
        previous = self.head
        current = previous.next
        for i in range(1, index):
            previous = previous.next
            current = current.next
        previous.next = node
        node.next = current.next
        current = None


    def sub_from_end(self, node):
        current = self.head
        while current.next.next:
            current = current.next
        current.next = node

    def sum(self):
        sum = 0
        if not self.head:
            return None
        current = self.head
        while current:
            sum += current.value
            current = current.next
        return sum


    def find(self, value):
        index = 0
        current = self.head
        while current:
            if current.value == value:
                return index
            index += 1
            current = current.next
        return None

    def display(self):
        if self.head:
            current = self.head
            print(current.value, ' -> ', end='')
        else:
            print('List is empty')
            return None
        while current.next:
            current = current.next
            print(current.value, ' -> ', end='')
        print('none')
