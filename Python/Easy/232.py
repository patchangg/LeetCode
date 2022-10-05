class MyQueue:

    def __init__(self):
        self.inQ = []
        self.outQ = []

    def push(self, x: int) -> None:
        self.inQ.append(x)

    def pop(self) -> int:
        self.peek()
        return self.outQ.pop()

    def peek(self) -> int:
        if self.outQ == []:
            while self.inQ:
                self.outQ.append(self.inQ.pop())
        return self.outQ[-1]

    def empty(self) -> bool:
        return self.inQ == [] and self.outQ == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
