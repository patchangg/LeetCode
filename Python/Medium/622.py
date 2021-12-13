class MyCircularQueue:

    def __init__(self, k: int):
        self.size = 0
        self.maxSize = k
        self.queue = [0]*k
        self.front = 0
        self.end = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.end = (self.end + 1) % self.maxSize
        self.queue[self.end] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.maxSize
        self.size -= 1
        return True

    def Front(self) -> int:
        # Returns the front element of the queue
        if self.size != 0:
            return self.queue[self.front]
        else:
            return -1

    def Rear(self) -> int:
        # Returns the rear element of the queue
        if self.size != 0:
            return self.queue[self.end]
        else:
            return -1

    def isEmpty(self) -> bool:
        # Check if the queue is empty
        return self.size == 0

    def isFull(self) -> bool:
        # Check if the queue is full
        return self.size == self.maxSize

# Create a array sized k and keep track of the front and end positions of the
# array. Adding elements to the queue just moves the front variable forward
# and puts the value into that position in the array.
# Removing a element is just moving the end variable backwards by 1, so getting
# the rear element is the variable behind the old one.
# O(1) time, O(k) space
# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
