import collections

class FindSumPairs:

    def __init__(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq = collections.Counter(nums2)

    def add(self, index, val):
        self.freq[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.freq[self.nums2[index]] += 1

    def count(self, tot):
        result = 0
        for i in self.nums1:
            result += self.freq[tot-i]
        return result

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
["FindSumPairs", "count", "add", "count", "count", "add", "add", "count"]
[[[1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]], [7], [3, 2], [8], [4], [0, 1], [1, 1], [7]]
