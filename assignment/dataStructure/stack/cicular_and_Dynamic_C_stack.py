class circular_stack:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.circular_array = [None] * self.capacity
        self.count = 0
        self.top = -1

    def is_empty(self):
        return self.count == 0
    def size(self):
        size=self.count
        return size

    def push(self, item):
        if self.count == self.capacity:
            self._resize()
        self.top = (self.top + 1) % self.capacity
        self.circular_array[self.top] = item
        self.count += 1
        return self.circular_array[self.top]

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return_value = self.circular_array[self.top]
        self.circular_array[self.top] = None
        self.top = (self.top - 1 + self.capacity) % self.capacity
        self.count -= 1
        return return_value

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.circular_array[self.top]

    def _resize(self):
        new_capacity = 2 * self.capacity
        new_stack = [None] * new_capacity
        for i in range(self.count):
            new_stack[i] = self.circular_array[(self.top - self.count + 1 + i) % self.capacity]
        self.circular_array = new_stack
        self.capacity = new_capacity
        self.top = self.count - 1

# Example usage
c_stack = circular_stack()
print(" every pushed element")
print(c_stack.push(1))
print(c_stack.push(2))
print(c_stack.push(3))
print(c_stack.push(4))
print(c_stack.push(5))
print(c_stack.push(45))
print(c_stack.push(78))
print("the top element is:")
print(c_stack.peek())
print("the size of the stack is:")
print(c_stack.size())
#print(c_stack.peek()) 
print(c_stack.pop())
print("the top element after pop is:")
print(c_stack.peek())
print("the poped element are:")
print(c_stack.pop())
print(c_stack.pop())  
print(c_stack.pop())  
print(c_stack.pop())  
print(c_stack.pop())  
print(c_stack.pop())  
print(c_stack.pop()) 
print("the size of the stack is:")
print(c_stack.size()) 



