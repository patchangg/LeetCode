from collections import defaultdict
import bisect

class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.hashmap = defaultdict(list)
        for i in range(len(arr)):
            self.hashmap[arr[i]].append(i)


    def query(self, left: int, right: int, value: int) -> int:
        indexs = self.hashmap[value]
        right = bisect.bisect(indexs,right)
        left = bisect.bisect_left(indexs,left)
        return right - left

# Create a hashmap that stores the index of each number in the array
# Binary search between the left and right index and check how many values
# are between the left and right index
# Input = ["RangeFreqQuery", "query", "query"]
# [[[12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]], [1, 2, 4], [0, 11, 33]]
# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
