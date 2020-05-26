
#Every Node has data and next

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_tail(self, value):
        new_node = Node(value)
        self.length += 1
        if self.head:
            self.head = new_node
            return
        tail_node = self.head
        while tail_node.next:
            tail_node = tail_node.next
        tail_node.next = new_node

    def contains(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next

    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value
