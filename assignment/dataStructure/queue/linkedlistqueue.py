class LinkedQueue:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None)
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            print('The queue is empty.')
        first_node = self._header._next
        return first_node._element

    def dequeue(self):
        if self.is_empty():
            print('The queue is empty.')
        first_node = self._header._next
        self._header._next = first_node._next
        self._size -= 1
        return first_node._element

    def enqueue(self, e):
        walk = self._header
        while walk._next is not None:
            walk = walk._next
        walk._next = self._Node(e, None)
        self._size += 1

    def concatenate(self, other):
        if type(self) != type(other):
            raise TypeError
        last_node = self._header
        while last_node._next is not None:
            last_node = last_node._next
        last_node._next = other._header._next
        other._header._next = None
        self._size += other._size
        other._size = 0
queue=LinkedQueue()
#queue.enqueue(4)
queue.dequeue()