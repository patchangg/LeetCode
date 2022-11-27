
def intersect(nums1, nums2):
    nums1 = sorted(nums1)
    nums2 = sorted(nums2)
    i = 0
    j = 0
    output = []

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums2[j] < nums1[i]:
            j += 1
        else:
            output.append(nums1[i])
            i += 1
            j += 1
    return output

nums1 = [1,2,2,1]
nums2 = [2,2]
intersection = intersect(nums1,nums2)
print(intersection)
