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
        
    def contains(self, value):
        temp = self.root
        while temp is not None:
            if (value < temp.value):
                temp = temp.left
                
            elif (value > temp.value):
                temp = temp.right
            else:
                return True
        return False
    
# simplified by ChatGPT
# def contains(self, value):
#     temp = self.root
#     while temp:
#         if value == temp.value:
#             return True
#         temp = temp.left if value < temp.value else temp.right
#     return False

        
myTree = BinarySearchTree()
myTree.insert(2)
myTree.insert(1)
myTree.insert(3)
myTree.insert(2)
myTree.insert(6)

print(myTree.contains(0))