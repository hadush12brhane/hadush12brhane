class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self,maxSize):
        self.front = None
        self.rear = None
        self.size=0
        self.maxSize=maxSize



    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False
    def isfull(self):
        if  self.size==self.maxSize:
            return True
        else:
            return False

    def enqueue(self, data):
        if self.size==self.maxSize:
            return False
        new_node = Node(data)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size+=1
    def dequeue(self):
        if self.is_empty(): 
            return "Queue is empty"
        data = self.front.data
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        self.size-=1
        return data

    def display(self):
        current = self.front
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
    def getSize(self):
        return self.size

# Example usage
q = Queue(5)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
print(q.isfull())
print("the size of the queue")
print(q.getSize())
q.display()  # Output: 1 2 3
print("output of the dequeue")

print(q.dequeue())  # Output: 1
#q.size()
print(q.dequeue())  # Output: 2
print("the size of the queue after dequeue")
print(q.getSize())
print("the queue after dequeue")
q.display()  # Output: 3
