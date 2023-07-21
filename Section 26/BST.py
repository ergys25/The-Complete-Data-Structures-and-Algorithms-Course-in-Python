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




newBST = BSTNode(None)
insert(newBST, 50)
insert(newBST, 20)
insert(newBST, 30)
insert(newBST, 60)
insert(newBST, 70)