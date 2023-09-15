#1 3
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None



class LinkedList:
    def __init__( self ) -> None:
        self.head =  None
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

    def append( self, value ):
        new_node = Node( value )
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1


    def add_head( self, value ):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert( self, value, index ):
        new_node = Node(value)
        temp_node = self.head
        for _ in range(index - 1):
            temp_node = temp_node.next
        new_node.next = temp_node.next
        temp_node.next = new_node
        self.length += 1

    def travers(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
    
    def search(self, target):
        current = self.head
        while current:
            if current.value == target:
                return True
            current = current.next
        return False

    def get(self , idx):
        if idx < 0 or idx >= self.length:
            return None
        current = self.head
        for _ in range(idx):
            current= current.next
        return current

    def set(self , idx, value):
        if idx < 0 or idx >= self.length:
            return None
        current = self.head
        for _ in range(idx):
            current= current.next
        current.value = value

    def pop_first(self):
        pop_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            pop_node.next = None
        self.length -= 1
        return pop_node


    def pop(self):
        pop_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        temp = self.head
        while temp.next is not self.tail:
            temp = temp.next
        self.tail = temp
        temp.next = None
        self.length -= 1
        return pop_node
    

    def remove(self, idx):
        if idx >= self.length or idx < 0:
            return None
        if idx == 0:
            return self.pop_first()
        prev_node = self.get(idx - 1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node
    
    def delete_all(self):
        self.head = None
        self.tail = None
        self.lengh = 0


new = LinkedList()
new.append(12)
new.append(12)
new.append(31)
new.add_head(1311)
new.insert(1, 3)
new.travers()
print(new)
print(new.get(4))
print(new.search(12))
print(new.set(1, 11))
print(new)
print(new.pop_first().value)
print(new)


