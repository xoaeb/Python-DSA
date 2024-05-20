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

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp.value

    def get(self, index):
        if index < 0 or index > self.length:
            return None
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp= self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp.value


my_doublylist = DoublyList(3)
my_doublylist.append(1)
my_doublylist.append(4)

my_doublylist.append(1)

my_doublylist.append(5)

# my_doublylist.prepend(0)
# print(my_doublylist.pop())
print('**get method gets***')
print(my_doublylist.get(4))
print('*-*-*')
my_doublylist.printList()
