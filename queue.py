class Queue:
    def __init__(self, length):
        self.items = []
        self.length = length

    def enqueue(self, item):
        if self.isFull():
            print("OverFlow")
        else:    
            self.items.append(item)

    def dequeue(self):
        if self.isEmpty():
            print("UnderFlow")
        else:
            return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def isFull(self):
        return len(self.items) == self.length 

    def front(self):
        if not self.isEmpty():
            return self.items[0]

    def rear(self):
        if not self.isEmpty():
            return self.items[-1]
        
    def getQueue(self):
        return self.items