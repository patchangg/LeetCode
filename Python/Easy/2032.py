from collections import Counter

def twoOutOfThree(nums1, nums2, nums3):
    nums1 = set(nums1)
    nums2 = set(nums2)
    nums3 = set(nums3)
    combined = Counter(list(nums1) + list(nums2) + list(nums3))
    output = []
    for num in combined.most_common():
        if num[1] > 1:
            output.append(num[0])
    return output

nums1 = [1,1,3,2]
nums2 = [2,3]
nums3 = [3]
inTwoOrMore = twoOutOfThree(nums1,nums2,nums3)
print(inTwoOrMore)
