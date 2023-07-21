class BSTNode:
    def __init__(self,data) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None






def insert(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insert(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insert(rootNode.rightChild, nodeValue)
    return "Inserted"

def preOrderTraversall(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversall(rootNode.leftChild)
    preOrderTraversall(rootNode.rightChild)

def inOrderTraversall(rootNode):
    if not rootNode:
        return
    inOrderTraversall(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversall(rootNode.rightChild)

def postOrderTraversall(rootNode):
    if not rootNode:
        return
    postOrderTraversall(rootNode.leftChild)
    print(rootNode.data)
    postOrderTraversall(rootNode.rightChild)

def levelOrdertraversall(rootNode):
    if not rootNode:
        return
    stack = []
    stack.append(rootNode)
    while not (len(stack) == 0):
        root = stack.pop()
        print(root.data)
        if root.leftChild is not None:
            stack.append(root.leftChild)
        if root.rightChild is not None:
            stack.append(root.rightChild)

def search(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print("The Valuse is found")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            print("The value is found")
        else:
            search(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild.data == nodeValue:
            print("The value is found")
        else:
            search(rootNode.rightChild, nodeValue)
        
    
    


newBST = BSTNode(None)
insert(newBST, 70)
insert(newBST, 50)
insert(newBST, 90)
insert(newBST, 30)
insert(newBST, 60)
insert(newBST, 80)
insert(newBST, 100)
insert(newBST, 20)
insert(newBST, 40)

preOrderTraversall(newBST)
inOrderTraversall(newBST)
postOrderTraversall(newBST)
inOrderTraversall(newBST)
search(newBST, 40)
