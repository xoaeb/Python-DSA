class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



class  BinarySearchTree:
    def __init__(self):
        self.root = None
        
        
    def insert(self, value):
        new_node = Node(value)
        
        if self.root  == None:
            self.root =new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value :
                return False
            if new_node.value < temp.value:
                if temp.left  == None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right  == None:
                    temp.right = new_node
                    return True
                temp = temp.right                 
        
        
myTree = BinarySearchTree()
myTree.insert(2)
myTree.insert(1)
myTree.insert(3)
myTree.insert(2)
myTree.insert(6)

# Safe printing to avoid None reference errors
print(myTree.root.value, 'root')  # Expected: 2
print(myTree.root.left.value, 'left')  # Expected: 1
if myTree.root.right:  # Check if right child exists
    print(myTree.root.right.value, 'right')  # Expected: 3
if myTree.root.right and myTree.root.right.right:  # Check if right child of right child exists
    print(myTree.root.right.right.value, 'right right')  # Expected: 6