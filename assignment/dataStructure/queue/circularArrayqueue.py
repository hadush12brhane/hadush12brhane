# Circular Queue implementation in Python


class CircularQueue():

    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.fornt = self.rear = -1
        self.count=0
    def isFull(self):
        if ((self.rear + 1) % self.k == self.fornt):
            return True
        else:
            return False

    # Insert an element into the circular queue
    def enqueue(self, data):
        if ((self.rear + 1) % self.k == self.fornt):
            self.isFull()
        elif(self.fornt == -1):
            self.fornt = 0
            self.rear = 0
            self.queue[self.rear] = data
            self.count+=1
        else:
            self.rear = (self.rear + 1) % self.k
            self.queue[self.rear] = data
            self.count+=1

    # Delete an element from the circular queue
    def isEmpty(self):
        if self.fornt==-1:
            print("The circular queue is empty\n")
            return True
        else:
            return False
    def dequeue(self):
        self.count=self.k
        if (self.fornt == -1):
            print("")

        elif (self.fornt == self.rear):
            temp = self.queue[self.fornt]
            self.fornt = -1
            self.rear = -1
            self.count-=1
            return temp
        else:
            temp = self.queue[self.fornt]
            self.fornt = (self.fornt + 1) % self.k
            self.count-=1
            return temp
    def size(self):
        sizeOfqueue=self.count
        return sizeOfqueue

    def printCQueue(self):
        if(self.fornt == -1):
            self.isEmpty()
        elif (self.rear >= self.fornt):
            for i in range(self.fornt, self.rear + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.fornt, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
            print()


# Your CircularQueue object will be instantiated and called as such:
obj = CircularQueue(5)
print("intial check for empty and print the list")
#print(obj.isEmpty())
obj.printCQueue()
obj.enqueue(1)
obj.enqueue(2)
print(obj.size(),end="<=size\n")
obj.enqueue(3)
obj.enqueue(4)
print("check if it is full or not in the middle ")
print(obj.isFull()) 
obj.enqueue(5)
obj.enqueue(6)
print("Initial queue")
obj.printCQueue()
print("The circular queue is fullor not \n")
print(obj.isFull())
print(obj.size(),end="<=size\n")
obj.dequeue()
print("After removing an element from the queue\n")
obj.printCQueue()
print(obj.size(),end="<=size\n")
print(obj.isFull())

