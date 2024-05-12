class Node:
    def __init__ (self, value):
        self.value= value
        self.next=None
        
class LinkedList:
    def __init__(self, value):
        new_node= Node(value)
        self.head=new_node
        self.tail= new_node
        self.length=1
        
        
    def append(self, value):
        new_node= Node(value)
        if self.head is None:
            self.head= new_node
            self.tail= new_node
        else:
            self.tail.next= new_node
            self.tail= new_node
        self.length +=1
        return True
    
    
    
    def pop(self):
        if self.length == 0:  # Check if the list is empty
            return None
        
        if self.length == 1:  # If there's only one node in the list
            value = self.head.value
            self.head = None
            self.tail = None
            self.length = 0
            return value

        pre = self.head
        temp = self.head
        while temp.next:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1  # Decrement the length by 1 after the node is popped
        return temp.value  # Return the value of the popped node

        
        
    def prepend(self, value):
        new_node= Node(value)
        if self.length == 0:
            self.head=new_node
            self.tail= new_node
        else:   
            new_node.next= self.head
            self.head=new_node
        self.length +=1

    def printList(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp= temp.next
        
        
mylinkedList = LinkedList(3)
mylinkedList.append(32)
mylinkedList.append(52)
# popednode=mylinkedList.pop()
# print( 'poped node is', popednode)
mylinkedList.prepend(1)
mylinkedList.printList()
