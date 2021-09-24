class FrontMiddleBackQueue:

    def __init__(self):
        self.queue = []

    def pushFront(self, val: int) -> None:
        self.queue.insert(0,val)

    def pushMiddle(self, val: int) -> None:
        self.queue.insert(int(len(self.queue)/2),val)

    def pushBack(self, val: int) -> None:
        self.queue.append(val)

    def popFront(self) -> int:
        if self.queue:
            return self.queue.pop(0)
        return -1

    def popMiddle(self) -> int:
        if self.queue:
            return self.queue.pop(int((len(self.queue)-1)/2))
        return -1

    def popBack(self) -> int:
        if self.queue:
            return self.queue.pop()
        return -1

# Python Insert at the location specified and append puts the integer at the
# back of the queue. Pop at the specified location or the back by default
# O(n), O(1) space for insert and pop with specifed index. O(1), O(1) space
# for default pop and append
# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
