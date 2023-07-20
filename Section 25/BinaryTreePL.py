class BinaryTree:
    def __init__(self, size) -> None:
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size



    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "Binary Tree is Full"
        self.customList[self.lastUsedIndex + 1] = value
        self.lastUsedIndex += 1
        return "The value has been succesfully inserted"


newBt = BinaryTree(8)
print(newBt.insertNode("Drinks"))
print(newBt.insertNode("hot"))
print(newBt.insertNode("cold"))
print(newBt.customList)