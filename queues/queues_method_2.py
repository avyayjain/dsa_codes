class Queue:
    def __init__(self, cap):
        self.queue = [None]*cap
        self.capacity = cap
        self.front = 0
        self.rear = self.capacity - 1
        self.curr_size = 0

    def is_full(self):
        if self.curr_size == self.capacity:
            print("OverFlow Condition, can't Enqueue")

        return self.curr_size == self.capacity

    def is_empty(self):
        if self.curr_size == 0:
            print("Underflow Condition, can't Dequeue")

        return self.curr_size == 0

    def enqueue(self, item):
        if self.is_full():
            return

        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.curr_size += 1
        print(self.queue[self.rear], " enqueued to queue")

    def dequeue(self):
        if self.is_empty():
            return

        item = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity

        self.curr_size -= 1

        print(item, " dequeued from queue")

    # function to display the queue
    def display(self):
        if self.curr_size == 0:
            print("Queue was Empty!!!")
        else:
            i = self.front
            j = 0
            print("Queue : ", end="")

            while j < self.curr_size:
                print(self.queue[(i + j) % self.capacity], end=" ")
                j += 1


# Driver Code
q = Queue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

print()
q.dequeue()
q.dequeue()
print()
q.enqueue(50)
q.enqueue(60)
q.enqueue(70)
print()


q.display()