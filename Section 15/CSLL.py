
"""
csll
"""

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
 
class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
 
    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next


    def createCSLL(self, value):
        node = Node(value=value)
        node.next = node
        node.head = node
        node.tail = node
