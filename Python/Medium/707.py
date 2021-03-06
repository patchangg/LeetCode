
class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    # Go through the nodes starting from the head until index is reached.
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        if self.head is None:
            return -1

        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val

    # Use the head of the linked list, create a new node, make it point to
    # the current head and make it the new head of the linked list
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(0, val)

    # Go through the linked list until the end and make it point to the new node
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    # Go through the linked list until the index, create the new node and make
    # the current nodes next be the new nodes next and make the current node
    # point to the new node
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return

        curr = self.head
        node = Node(val)

        if index <= 0:
            node.next = curr
            self.head = node
        else:
            for i in range(index - 1):
                curr = curr.next
            node.next = curr.next
            curr.next = node
        self.size += 1

    # Go through the linked list until the index, make the current node point
    # to the next nodes next to remove the next node from the linked list.
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return -1

        curr = self.head
        if index == 0:
            self.head = curr.next
        else:
            for i in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next
        self.size -= 1

# Get() and addHead are O(1), rest is O(n). O(n) space
# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
param_1 = obj.get(index)
obj.addAtHead(val)
obj.addAtTail(val)
obj.addAtIndex(index,val)
obj.deleteAtIndex(index)
