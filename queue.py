class Node:
    def __init__(self, value):
        self.value =value
        self.next = None

class Queue:
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def printQueue(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next


myQueue =  Queue(1)
myQueue.printQueue()