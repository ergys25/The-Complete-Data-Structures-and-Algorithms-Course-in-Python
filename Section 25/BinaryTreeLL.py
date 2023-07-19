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
            
            










preOrderTraversal(newBT)
inOrderTraversal(newBT)
postOrderTraversal(newBT)
levelOrderTraversal(newBT)