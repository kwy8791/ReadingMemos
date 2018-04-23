class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

q1 = Queue()
print(q1.is_empty())


q2 = Queue()
for i in range(5):
    q2.enqueue(i)

print(q2.size())


q3 = Queue()
for i in range(5):
    q3.enqueue(i)

while q3.size():
    print(q3.dequeue())

print()
print(q3.size())
