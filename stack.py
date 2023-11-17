class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if self.stack:
            return True
        return False

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop(-1)

    def size(self):
        return len(self.stack)
    
    def top(self):
        return self.stack[-1]

stack = Stack()

print("Is the stack empty?", stack.is_empty())

stack.push(1)
stack.push(2)
stack.push(3)

print("Stack size:", stack.size())
print("Top of the stack:", stack.top())

popped_item = stack.pop()
print("Popped item:", popped_item)
print("Stack size after popping:", stack.size())