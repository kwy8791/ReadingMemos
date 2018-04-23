class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items) - 1
        return self.items[last]

    def size(self):
        return len(self.items)

stack1 = Stack()
print(stack1.is_empty())

stack2 = Stack()
stack2.push(1)
print(stack2.is_empty())

stack3 = Stack()
stack3.push(1)
item = stack3.pop()
print(item)
print(stack3.is_empty())

stack4 = Stack()

for i in range(0, 6):
    stack4.push(i)

print(stack4.peek())
print(stack4.size())
