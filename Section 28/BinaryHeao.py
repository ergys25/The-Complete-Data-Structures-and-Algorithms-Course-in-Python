class Heap:
     def __init__(self,size) -> None:
          self.customList = (size + 1) * None
          self.heapSize = 0
          self.maxSize = size + 1

def peek(rootNode):
     if not rootNode:
          return
     else:
          return rootNode.customList[1]

newBH = Heap(5)


