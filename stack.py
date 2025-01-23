class Node:
    def __init__(self, value):
        self.value =value
        self.next = None

class Stack:
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def printStack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next


    def push(self,value):
        new_node = Node(value)
        if(self.height ==0):
            self.top = new_node
        else:
            new_node.next = self.top
            self.top= new_node
        self.height  +=1
        return 

    def pop(self):
        if self.height == 0: 
            return None
        temp = self.top
        if self.height == 1:
            self.top = None
        else:
            self.top = self.top.next
            temp.next = None
        self.height -= 1
        return temp    
        
        
myStack =  Stack(1)
myStack.push(2)
myStack.push(3)
myStack.push(4)
myStack.push(5)

myStack.printStack()
popped1 = myStack.pop()
popped2 = myStack.pop()
# myStack.pop()
print(popped1.value,'<----popped node')
print(popped2.value,'<----popped node')
myStack.printStack()
