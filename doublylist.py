class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True


my_doublylist = DoublyList(3)
my_doublylist.append(9)

my_doublylist.printList()
