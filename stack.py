class Stack:
    def __init__(self, length):
        self.items = []
        self.length = length

    def push(self, item):
        if self.isFull():
            print("OverFlow")
        else:
            self.items.append(item)
    
    def pop(self):
        if self.isEmpty():
            print("UnderFlow")
        else:
            return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def isFull(self):
        return len(self.items) == self.length

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]

    def getstack(self):
        return self.items