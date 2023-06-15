class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None



class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp = self.head
        result = ''
        while temp is not None:
            result += str(temp.value)
            if temp.next is not None:
                result += '->'
            temp = temp.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1


    def add_head(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(self, value, index):
        new_node = Node(value)
        temp_node = self.head
        for _ in range(index - 1):
            temp_node = temp_node.next
        new_node.next = temp_node.next
        temp_node.next = new_node
        self.length += 1







new = LinkedList()
new.append(12)
new.append(12)
new.append(31)
new.add_head(1311)
new.insert(1, 3)
print(new)
