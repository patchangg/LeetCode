from itertools import combinations

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.combinationLength = combinationLength
        self.perm = list(combinations(characters,combinationLength))
        self.current = self.perm[0]
        self.count = 0

    def next(self) -> str:
        self.current = self.perm[self.count]
        self.count += 1
        return "".join(self.current)

    def hasNext(self) -> bool:
        if self.count + 1 <= len(self.perm):
            return True
        else:
            return False

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# ["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
# [["abc", 2], [], [], [], [], [], []]

itr = CombinationIterator("abc", 2);
itr.next();    # return "ab"
itr.hasNext(); # return True
itr.next();    # return "ac"
itr.hasNext(); # return True
itr.next();    # return "bc"
itr.hasNext(); # return False
