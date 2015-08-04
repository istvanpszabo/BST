__author__ = 'iszabo'

# This is the Node class, all of the functions happen here
class Node:
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None


    # If the value is already in the
    def insert(self, data):
        # The data already exists, it wont be inserted
        if self.value == data:
            return False
        # It checks whether the value bigger than the existing node, if yes it checks whether the left node exists
        # in case of yes it starts the process from the beginning for the node
        # if doesnt exist the left child, it will create a new node there
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True
        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    # It checkes whether the root already exists, when it doesnt, False can be returned directly.
    def find(self, data):
        if(self.value == data):
            return True
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

    # This is also a recursive traversal function. It prints the main node than the left when it exists and than the right when it exists.
    def preorder(self):
        if self:
            print(str(self.value))
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.value))

    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.value))
            if self.rightChild:
                self.rightChild.inorder()

# This is the implementation of the Tree itself and this just masks the real functions related to the Node class
class Tree:

    # Instantiating the class
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        print("PreOrder")
        self.root.preorder()

    def postorder(self):
        print("PostOrder")
        self.root.postorder()

    def inorder(self):
        print("InOrder")
        self.root.inorder()

bst = Tree()
print(bst.insert(10))