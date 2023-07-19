class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None



newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftChild.leftChild = tea
leftChild.rightChild = coffee
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild


def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data +'Pre')
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)



def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data +"IN")
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data + "Post")

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = []
        customQueue.append(rootNode)
        while not(len(customQueue)==0):
            root = customQueue.pop()
            print(root.data)
            if(root.leftChild is not None):
                customQueue.append(root.leftChild)
            if(root.rightChild is not None):
                customQueue.append(root.rightChild)
            
            

def search(rootNode, nodevalue):
    if not rootNode:
        return
    else:
        customQueue = []
        customQueue.append(rootNode)
        while not(len(customQueue)==0):
            root = customQueue.pop()
            if root.data == nodevalue:
                return "success"
            if(root.leftChild is not None):
                customQueue.append(root.leftChild)
            if(root.rightChild is not None):
                customQueue.append(root.rightChild)
        return "Not Found"
            

def insert(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = []
        customQueue.append(rootNode)
        while not(len(customQueue) == 0):
            root = customQueue.pop()
            if root.leftChild is not None:
                customQueue.append(root.leftChild)
            else:
                root.leftChild = newNode
                return "Success"
            if root.rightChild is not None:
                customQueue.append(root.rightChild)
            else: 
                root.rightChild = newNode
                return "Success"










preOrderTraversal(newBT)
inOrderTraversal(newBT)
postOrderTraversal(newBT)
levelOrderTraversal(newBT)
print(search(newBT, "Tea"))
print(search(newBT, "Cola"))
newNode = TreeNode("Cola")
insert(newBT, newNode)
levelOrderTraversal(newNode)