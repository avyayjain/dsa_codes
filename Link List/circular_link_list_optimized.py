class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        # if trying to enter the first node itself
        if self.head == None:
            self.head = new_node
            new_node.next = new_node
            return

            # add element just after the head node
        # swap data values of new_node and head node
        new_node.next = self.head.next
        self.head.next = new_node
        self.head.data, new_node.data = new_node.data, self.head.data

    def insert_last(self, data):
        new_node = Node(data)

        # if trying to enter the first node itself
        if self.head == None:
            self.head = new_node
            new_node.next = new_node
            return

            # add element just after the head node
        # swap data values of new_node and head node
        new_node.next = self.head.next
        self.head.next = new_node
        self.head.data, new_node.data = new_node.data, self.head.data
        self.head = new_node

    def display(self):
        temp = self.head
        if temp == None:
            return

        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break

            # Drive Code


ll = LinkedList()

ll.insert(12)
ll.insert(16)
ll.insert(20)

ll.insert(24)
ll.insert(30)
ll.insert(22)
ll.insert_last(42)
ll.display()
