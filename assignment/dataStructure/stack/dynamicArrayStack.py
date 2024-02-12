"""class Stack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, data):
        self.stack.append(data)
        if not self.min_stack or data <= self.min_stack[-1]:
            self.min_stack.append(data)

    def pop(self):
        if not self.stack:
            print("Stack Underflow")
            return None
        data = self.stack.pop()
        if data == self.min_stack[-1]:
            self.min_stack.pop()
        return data

    def peek(self):
        if not self.stack:
            print("Stack is empty")
            return None
        return self.stack[-1]

    def get_min(self):
        if not self.min_stack:
            print("Stack is empty")
            return None
        return self.min_stack[-1]

stack = Stack()
stack.push(3)
stack.push(5)
stack.push(2)
stack.push(1)
stack.push(4)
print(stack.pop()) # 4
print(stack.pop()) # 1
print(stack.get_min()) # 2
print(stack.pop()) # 2
print(stack.peek()) # 5
print(stack.pop()) # 5
print(stack.pop()) # 3
print(stack.pop()) # Stack Underflow
"""
"""
Max = 5
arr = [0]*Max
minEle = 0
Top = 0
def empty():
	if (Top <= 0):
		return True
	else:
		return False

# Method to push elements
# to the Special Stack
def push(x):
	global arr, Top, Max, minEle
	# If stack is empty
	if empty():
		# Assign x to minEle
		minEle = x
		# Assign x to arr[top]
		arr[Top] = x
		# Increment top by 1
		Top+=1
	# If array is full
	elif (Top == Max):

		# Update the Max size
		Max = 2 * Max

		temp = [0]*Max

		# Traverse the array arr[]
		for i in range(Top):
			temp[i] = arr[i]

		# If x is less than minEle
		if (x < minEle):
			# Push 2*x-minEle
			temp[Top] = 2 * x - minEle

			# Assign x to minEle
			minEle = x

			Top+=1
		# Else
		else:
			# Push x to stack
			temp[Top] = x
			Top+=1
		# Assign address of the
		# temp to arr
		arr = temp
	else:
		# If x is less
		# than minEle
		if (x < minEle):
			# Push 2*x-minEle
			arr[Top] = 2 * x - minEle
			Top+=1

			# Update minEle
			minEle = x
		else:
			# Push x to the
			# stack
			arr[Top] = x
			Top+=1

# Method to pop the elements
# from the stack.
def pop():
	global Top, minEle

	# If stack is empty
	if empty():
		print("Underflow")
		return
	# Stores the top element
	# of the stack
	t = arr[Top - 1]

	# If t is less than
	# the minEle
	if (t < minEle) :
		# Pop the minEle
		print("Popped element :", minEle)

		# Update minEle
		minEle = 2 * minEle - t
	# Else
	else:
		# Pop the topmost element
		print("Popped element :", t)
	Top-=1
	return

# Method to find the topmost
# element of the stack
def peek():
	# If stack is empty
	if empty():
		print("Underflow")
		return -1

	# Stores the top element
	# of the stack
	t = arr[Top - 1]

	# If t is less than
	# the minEle
	if (t < minEle):
		return minEle
	# Else
	else:
		return t

# Method to find the Minimum
# element of the Special stack
def getMin():
	# If stack is empty
	if empty():
		print("Underflow")
		return -1
	# Else
	else:
		return minEle

push(10)
push(4)
push(9)
push(6)
push(5)

print("Top Element :", peek())

print("Minimum Element :", getMin())

pop()
pop()
pop()
pop()

print("Top Element :", peek())
print("Minimum Element :", getMin())

# This code is contributed by mukesh07.
    """
class dynamic_stack:
    def __init__(self, capacity=1):
        self.capacity = capacity
        self.dynamic_stack = [None] * self.capacity
        self.top = 0
        self.count=0

    def is_empty(self):
        if self.top==0:
            print("the top is zero")
        return self.top==0
    def size(self):
        size=self.count
        return size

    def push(self, item):
        if self.top == self.capacity:
            self.everyTimeResizer()
        self.dynamic_stack[self.top] = item
        self.top += 1
        self.count+=1
        

    def pop(self):
        if self.is_empty():
            return "underflow"
        self.top -= 1
        to_be_poped = self.dynamic_stack[self.top]
        self.dynamic_stack[self.top] = None
        self.count-=1
        return to_be_poped

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.dynamic_stack[self.top - 1]

    def everyTimeResizer(self):
        new_capacity = 2 * self.capacity
        new_stack = [None] * new_capacity
        for i in range(self.top):
            new_stack[i] = self.dynamic_stack[i]
        self.dynamic_stack = new_stack
        self.capacity = new_capacity

#  usage
obj_stack = dynamic_stack()
print(obj_stack.is_empty())
obj_stack.push(1)
obj_stack.push(2)
obj_stack.push(3)
obj_stack.push(4)
obj_stack.push(6)
print("size")
print(obj_stack.size())
print("the top elemet to be poped is :")
print(obj_stack.pop())  # Output: 6
print("the updated top element after pop is:")
print(obj_stack.peek())  # Output: 4
