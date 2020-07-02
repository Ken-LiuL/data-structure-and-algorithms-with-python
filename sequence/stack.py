class Stack:
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def pop(self):
        if self.empty():
            raise RuntimeError('Attempt to pop from an empty stack')

        item  = self.items[-1]
        del self.items[-1]
        return item

    def push(self, item):
        self.items.append(item)

    def top(self):
        if self.empty:
            raise RuntimeError('Attempt to get top of empty stack')
        return self.items[-1]
