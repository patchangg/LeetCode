import random

class RandomizedSet:

    def __init__(self):
        self.randSet = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        if val not in self.randSet:
            self.randSet.append(val)
            self.pos[val] = len(self.randSet) - 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.randSet:
            index = self.pos[val]
            last = self.randSet[-1]
            self.randSet[index] = last
            self.pos[last] = index
            self.randSet.pop()
            del self.pos[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.randSet)

# Insert: Check if the val is in the array, if not append to it. O(1), O(1) space
# Remove: Swap the val and the last position and then pop it. O(1), O(1) space
# getRandom: inbuilt Python random list getter. O(1), O(1) space
RandomizedSet randomizedSet = RandomizedSet();
randomizedSet.insert(1); # Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); # Returns false as 2 does not exist in the set.
randomizedSet.insert(2); # Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); # getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); # Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); # 2 was already in the set, so return false.
randomizedSet.getRandom(); # Since 2 is the only number in the set, getRandom() will always return 2.
# output = [null, true, false, true, 2, true, false, 2]
