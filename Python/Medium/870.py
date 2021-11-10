from collections import deque

def advantageCount(nums1, nums2):
    nums1 = deque(sorted(nums1,reverse=True))
    nums2 = sorted([(num,index) for index,num in enumerate(nums2)],reverse=True)
    output = [-1] * len(nums1)
    for num, index in nums2:
        if nums1[0] > num:
            output[index] = nums1.popleft()
        else:
            output[index] = nums1.pop()
    return output

# Sort nums1 and nums2 descending with nums2 keeping the index.
# For each number in nums2, check if the number is smaller or greater than the
# first number in nums1. Pop if greater, popleft if smaller.
# This will maximise the number to put in the array. O(nlogn), O(n) space
nums1 = [2,7,11,15]
nums2 = [1,10,4,11]
maximumAdvantage = advantageCount(nums1,nums2)
print(maximumAdvantage)
