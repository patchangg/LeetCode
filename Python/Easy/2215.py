
def findDifference(nums1, nums2):
    output = []
    output.append(list(set(nums1) - set(nums2)))
    output.append(list(set(nums2) - set(nums1)))
    return output

nums1 = [1,2,3]
nums2 = [2,4,6]
difference = findDifference(nums1,nums2)
print(difference)
