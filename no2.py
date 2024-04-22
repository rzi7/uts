class Queue:
    def _init_(self, maxSize):
        self.queue = [None] * maxSize
        self.head = 0
        self.tail = -1
        self.maxSize = maxSize

    def initialize_queue(self):
        self.head = 0
        self.tail = -1

    def push(self, item):
        if self.tail == self.maxSize - 1:
            print("Queue is full")
        else:
            self.tail += 1
            self.queue[self.tail] = item

    def pop(self):
        if self.head > self.tail:
            print("Queue is empty")
        else:
            self.head += 1

    def front(self):
        if self.head > self.tail:
            print("Queue is empty")
        else:
            return self.queue[self.head]

    def is_empty(self):
        if self.head > self.tail:
            return True
        else:
            return False

# Contoh penggunaan
q = Queue(5)
q.push(1)
q.push(2)
q.push(3)
print("Front element:", q.front())
q.pop()
print("Front element after pop:", q.front())
print("Is queue empty?", q.is_empty())
