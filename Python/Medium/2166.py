class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.bits = [False] * size
        self.flipped = [True] * size
        self.bitCount = 0

    def fix(self, idx: int) -> None:
        if not self.bits[idx]:
            self.bits[idx] = True
            self.flipped[idx] = False
            self.bitCount += 1

    def unfix(self, idx: int) -> None:
        if self.bits[idx]:
            self.bits[idx] = False
            self.flipped[idx] = True
            self.bitCount -= 1

    def flip(self) -> None:
        self.bits, self.flipped = self.flipped, self.bits
        self.bitCount = self.size - self.bitCount

    def all(self) -> bool:
        return self.size == self.bitCount

    def one(self) -> bool:
        return self.bitCount > 0

    def count(self) -> int:
        return self.bitCount

    def toString(self) -> str:
        return "".join(['1' if bit else "0" for bit in self.bits])

# Create two boolean array where True means 1 and False means 0 sized size
# where one represents the bits and other flipped. init and toString are O(n)
# O(n) space, rest are O(1), O(1) space
# Your Bitset object will be instantiated and called as such:
obj = Bitset(size)
obj.fix(idx)
obj.unfix(idx)
obj.flip()
param_4 = obj.all()
param_5 = obj.one()
param_6 = obj.count()
param_7 = obj.toString()
