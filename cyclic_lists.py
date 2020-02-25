from linked_list import List


class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value


class CyclicList(List):

    def __init__(self):
        self.head = None

    def insert_to_begin(self, node):
        if self.head:
            node.next = self.head
            self.head.prev = node
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = node
            node.prev = current
            self.head = node
        else:
            node.next = node
            node.prev = node
            self.head = node

    def insert_to_end(self, node):
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = node
        node.prev = current
        node.next = self.head

    def insert_to_middle(self, node, index):
        previous = self.head
        current = previous.next
        for i in range(1, index):
            previous = previous.next
            current = current.next
        previous.next = node
        node.prev = previous
        node.next = current

    def delete_from_begin(self):
        current = self.head
        current = current.next
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        current.prev = temp
        self.head = current

    def delete_from_middle(self, index):
        previous = self.head
        current = previous.next
        for i in range(1, index):
            previous = previous.next
            current = current.next
        current = current.next
        previous.next = current
        current.prev = previous

    def delete_from_end(self):
        current = self.head
        while current.next.next != self.head:
            current = current.next
        current.next = self.head

    def sub_from_begin(self, node):
        if self.head:
            self.head.value = node.value
        else:
            self.head = node
        # current = None

    def sub_from_middle(self, node, index):
        previous = self.head
        current = previous.next
        for i in range(1, index):
            previous = previous.next
            current = current.next
        current = current.next
        previous.next = node
        node.prev = previous
        node.next = current
        current.prev = node

    def sub_from_end(self, node):
        current = self.head
        while current.next.next != self.head:
            current = current.next
        current.next = node
        node.prev = current
        node.next = self.head

    def sum(self):
        sum = 0
        if not self.head:
            return None
        current = self.head
        sum = current.value
        current = current.next
        while current != self.head:
            sum += current.value
            current = current.next
        return sum

    def find(self, value):
        index = 0
        current = self.head
        if current.value == value:
            return index
        current = current.next
        index += 1
        while current != self.head:
            if current.value == value:
                return index
            index += 1
            current = current.next
        return None

    def display(self):
        if self.head:
            current = self.head
            print(current.value, ' <-> ', end='')
        else:
            print('List is empty')
            return None
        while current.next != self.head:
            current = current.next
            print(current.value, ' <-> ', end='')
        print(self.head.value)
