
def numTriplets(nums1, nums2):
    freq1 = {}
    freq2 = {}
    output = 0
    for num in nums1:
        if num * num not in freq1:
            freq1[num*num] = 1
        else:
            freq1[num*num] += 1

    for num in nums2:
        if num * num not in freq2:
            freq2[num*num] = 1
        else:
            freq2[num*num] += 1

    for i in range(len(nums1)-1):
        for j in range(i+1, len(nums1)):
            triple = nums1[i] * nums1[j]
            if triple in freq2:
                output += freq2[triple]

    for i in range(len(nums2)-1):
        for j in range(i+1, len(nums2)):
            triple = nums2[i] * nums2[j]
            if triple in freq1:
                output += freq1[triple]
    return output

# Store the squared of each number in the arrays in a hashmap.
# Go through both arrarys, finding if nums[i] * nums[j] is in the hashmap,
# if so add the frequency amount to the output. O(nlogn), O(n) space
nums1 = [7,4]
nums2 = [5,2,8,9]
tripleNum = numTriplets(num1,nums2)
print(tripleNum)
