class SnapshotArray:

    def __init__(self, length: int):
        self.snapshot = {i: {0: 0} for i in range(length)}
        self.counter = 0

    def set(self, index: int, val: int) -> None:
        self.snapshot[index][self.counter] = val

    def snap(self) -> int:
        self.counter += 1
        return self.counter  - 1

    def get(self, index: int, snap_id: int) -> int:
        while snap_id > 0 and snap_id not in self.snapshot[index]:
            snap_id -= 1
        return self.snapshot[index][snap_id]

# Create a snapshot array that stores hashmaps.
# Use the hashmap to store the value of the index at that snapshot point
# and return the number stored at the snapshot point.
# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
