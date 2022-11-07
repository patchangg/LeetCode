from collections import deque

class MyStack:

    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.appendleft(x)

    def pop(self) -> int:
        return self.stack.popleft()

    def top(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        if self.stack:
            return False
        return True


# Your MyStack object will be instantiated and called as such:
myStack = MyStack()
myStack.push(1)
myStack.push(2)
topE = myStack.top()
print(topE)
popE = myStack.pop()
print(popE)
isEmpty = myStack.empty()
print(isEmpty)
