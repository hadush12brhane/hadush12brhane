class array_Stack:
    def __init__(self, SizeOarray):
        self.SizeOarray = SizeOarray
        self.array_Stack = [None] * SizeOarray
        self.top = 0
        self.count=0
    def is_empty(self):
        if self.top==0:
            print("the stack is empty")
    def is_full(self):
        if self.top==self.SizeOarray:
            print("the stack is full")
    def push(self, data):
        if self.top == self.SizeOarray - 1:
            print("Stack Overflow")
            return
        self.top += 1
        self.count+=1
        self.array_Stack[self.top] = data

    def pop(self):
        if self.top == 0:
            print("Stack Underflow")
            return
        data = self.array_Stack[self.top]
        self.top -= 1
        self.count-=1
        #print(data)
        return data
    def get_size(self):
        if self.is_empty():
            return 0
        elif self.is_full():
            return self.count==self.SizeOarray
        else:
            return self.count

    def peek(self):
        if self.top == 0:
            print("Stack is empty")
            return None
        return self.array_Stack[self.top]

stack = array_Stack(5)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
#stack.push(6) # Stack Overflow
print("the size is:")
print(stack.get_size())
print("check if it is full or not")
stack.is_full()
stack.push(7) 
stack.push(8) 
print("the top element before pop is:")
print(stack.peek()) # 3
print("the poped element is:")
print(stack.pop()) # 5
print("the poped element is:")
print(stack.pop()) # 4
print("the poped element is:")
print(stack.pop()) # 3print("the poped element is:")
print("the poped element is:")
print(stack.pop()) # 2
print("the size is:")
print(stack.get_size())
print("the poped element is:")
print(stack.pop()) # 1
print(stack.pop()) # Stack Underflow
