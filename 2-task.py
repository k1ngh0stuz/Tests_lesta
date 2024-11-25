# 2 - task

# 1 option
class Circularbuffer:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Содержимое должна быть больше нуля.")
        self.buffer = [None] * capacity
        self.capacity = capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Буфер заполнен!")
        self.buffer[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Буфер пуст!")
        value = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return value

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def __repr__(self):
        return f"Circularbuffer({self.buffer}, head={self.head}, tail={self.tail}, size={self.size})"


# 2 option
from collections import deque


class CircularQueue:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Содержимое должна быть больше нуля.")
        self.capacity = capacity
        self.buffer = deque(maxlen=capacity)

    def enqueue(self, value):
        if len(self.buffer) == self.capacity:
            raise OverflowError("Буфер заполнен!")
        self.buffer.append(value)

    def dequeue(self):
        if len(self.buffer) == 0:
            raise IndexError("Буфер пуст!")
        return self.buffer.popleft()

    def is_empty(self):
        return len(self.buffer) == 0

    def is_full(self):
        return len(self.buffer) == self.capacity

    def __repr__(self):
        return f"CircularQueue({list(self.buffer)})"
