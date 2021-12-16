
def maxDistance(nums1, nums2):
    output = 0
    i = 0
    for j, num in enumerate(nums2):
        while i < len(nums1) and nums1[i] > num:
            i += 1
        if i == len(nums1):
            break
        output = max(output,j-i)
    return output

# While looping through nums2, find the index where the number in nums2 is >=
# to the number in nums1 and check if the distance between the index in nums2
# and the index in nums1 that contains the smaller number is the maximum found.
# Return the maximum distance. O(n + m) where n is the length of nums1 and m
# is the length of nums2, O(1) space.
nums1 = [55,30,5,4,2]
nums2 = [100,20,10,10,5]
maximumDistance = maxDistance(nums1,nums2)
print(maximumDistance)
