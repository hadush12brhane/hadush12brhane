class Stack:
    def __init__(self, sizeOfArray):
        self.sizeOfArray = sizeOfArray
        self.stack = [None] * sizeOfArray
        self.top = -1
        self.size=0

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def is_full(self):
        if  self.top == self.sizeOfArray - 1:
            return True
        else:
            return False

    def push(self, data):
        if self.is_full():
            return False
        self.top = (self.top + 1) % self.sizeOfArray
        self.stack[self.top] = data
        self.size+=1
        return True

    def pop(self):
        if self.is_empty():
            return None
        data = self.stack[self.top]
        self.stack[self.top] = None
        self.top = (self.top - 1) % self.sizeOfArray
        self.size-=1
        return data

    """def peek(self):
        if self.is_empty():
            return None
        return self.stack[self.top]"""
    def getSize(self):
        return self.size

s = Stack(6)
print(s.is_empty())
s.push(1)
s.push(2)
s.push(3)
s.push(6)
s.push(8)
print(s.getSize())
print(s.is_full())
print("poped elements are:")
print(s.pop())
print(s.pop())
print("the size after pop is ")
print(s.getSize())

