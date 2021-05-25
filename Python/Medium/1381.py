class CustomStack:
    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) + 1 <= self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        if k > len(self.stack):
            for i in range(len(self.stack)):
                self.stack[i] += val
        else:
            for i in range(k):
                self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
customStack = CustomStack(3) # Stack is Empty []
customStack.push(1)                        # stack becomes [1]
customStack.push(2)                          # stack becomes [1, 2]
customStack.pop()                           # return 2 --> Return top of the stack 2, stack becomes [1]
customStack.push(2)                          # stack becomes [1, 2]
customStack.push(3)                          # stack becomes [1, 2, 3]
customStack.push(4)                          # stack still [1, 2, 3], Don't add another elements as size is 4
customStack.increment(5, 100)                # stack becomes [101, 102, 103]
customStack.increment(2, 100)                # stack becomes [201, 202, 103]
customStack.pop()                            # return 103 --> Return top of the stack 103, stack becomes [201, 202]
customStack.pop()                            # return 202 --> Return top of the stack 102, stack becomes [201]
customStack.pop()                            # return 201 --> Return top of the stack 101, stack becomes []
customStack.pop()                            # return -1 --> Stack is empty return -1.
