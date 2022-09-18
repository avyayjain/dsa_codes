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
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            return

        curr = self.head
        # Traverse till the end of LL
        while curr.next != self.head:
            curr = curr.next

        curr.next = new_node
        new_node.next = self.head
        self.head = new_node

    def insert_last(self, data):
        new_node = Node(data)

        # if trying to enter the first node itself
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            return

        curr = self.head
        # Traverse till the end of LL
        while curr.next != self.head:
            curr = curr.next

        curr.next = new_node
        new_node.next = self.head

    def deleteStart(self):

        # if LL is already empty
        if self.head is None:
            print("LL empty, nothing to delete")
            return

            # if there is only one node present
        if self.head.next == self.head:
            print("Node deleted: ", self.head.data)  # will be deleted in next line
            self.head = None
            return

            # go to last node
        curr = self.head
        while curr.next != self.head:
            curr = curr.next

        curr.next = self.head.next  # last node in LL points to next node of current head
        print("Node deleted: ", self.head.data)  # will delete in next line
        self.head = self.head.next  # head shifted to next node

        # deletion of the previous head handled by garbage collector

    def display(self):
        temp = self.head
        if temp is None:
            return

        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print()

            # Drive Code


ll = LinkedList()

ll.insert(12)
ll.insert(16)
ll.insert(20)

ll.insert(24)
ll.insert(30)
ll.insert(22)
ll.insert_last(24)
ll.display()
ll.deleteStart()

ll.display()
