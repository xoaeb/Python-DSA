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

    # def pop(self):
    #     if self.length == 0:
    #         return None
    #     if self.length == 1:
    #         return self.head
    #     else:
    #         temp = self.tail
    #         self.tail = self.tail.prev
    #         self.tail.next = None
    #         temp.prev = None
    #         self.length-=1
    #         return temp.value
    #     return True

    # better solution 👇👇

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None

        self.length -= 1
        return temp


my_doublylist = DoublyList(3)
my_doublylist.append(9)
my_doublylist.append(71)
print(my_doublylist.pop())
my_doublylist.printList()
