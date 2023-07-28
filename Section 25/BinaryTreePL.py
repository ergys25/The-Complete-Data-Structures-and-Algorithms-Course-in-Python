"""btpl"""
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
    
    def Search(self, nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return "Success"
        return("Not Found")
    
    def preOrder(self, index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrder(index * 2)
        self.preOrder(index *  2 + 1)

    def inOrder(self, index):
        if index > self.lastUsedIndex:
            return 
        self.inOrder(index * 2)
        print(self.customList[index])
        self.inOrder(index *  2 + 1)
        

    def postOrder(self, index): 
        if index > self.lastUsedIndex:
            return
        self.postOrder(index * 2)
        self.postOrder(index *  2 + 1)
        print(self.customList[index])
    

    def levelOrder(self, index):
        for i in range (index, self.lastUsedIndex + 1):
            print(self.customList[i])

    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            return
        for i in range(1, self.lastUsedIndex + 1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self. lastUsedIndex -= 1
                return


    def Delete(self):
        self.customList = None
        return








newBt = BinaryTree(8)
print(newBt.insertNode("Drinks"))
print(newBt.insertNode("hot"))
print(newBt.insertNode("cold"))
print(newBt.insertNode("tea"))
print(newBt.insertNode("coffee"))

print(newBt.customList)
print(newBt.Search("hot"))
newBt.preOrder(1)
newBt.inOrder(1)
newBt.postOrder(1)
newBt.levelOrder(1)