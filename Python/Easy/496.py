
def nextGreaterElement(nums1, nums2):
    output = []
    for num in range(len(nums1)):
        greater = False
        for i in range(len(nums2)):
            if nums2[i] == nums1[num]:
                for s in range(i+1,len(nums2)):
                    if nums2[s] > nums1[num]:
                        output.append(nums2[s])
                        greater = True
                        break
        if not greater:
            output.append(-1)
    return output




nums1 = [4,1,2]
nums2 = [1,3,4,2]
nextG = nextGreaterElement(nums1,nums2)
print(nextG)
